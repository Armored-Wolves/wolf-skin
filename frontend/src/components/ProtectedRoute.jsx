// здесь осущетствляется проверка токена до перенаправления на страницу для автор-ных п-лей
import { Navigate } from "react-router-dom";
import { jwtDecode } from "jwt-decode";
import api from "../api";
import { REFRESH_TOKEN, ACCESS_TOKEN } from "../constants";
import { useState, useEffect } from "react";

function ProtectedRoute({ children }) {
    const [isAuthorized, setIsAuthorized] = useState(null);

    useEffect(() => { auth().catch(() => setIsAuthorized(false)) }, []);

    const refreshToken = async () => {                    // функия для автоматического обновления refresh token
        const refreshToken = localStorage.getItem(REFRESH_TOKEN);
        try {
            const res = await api.post("http://127.0.0.1:8000/api/token/refresh", {
                refresh: refreshToken,
            });
            if (res.status === 200) {
                localStorage.setItem(ACCESS_TOKEN, res.data.access);
                setIsAuthorized(true);
            }
            else {
                setIsAuthorized(false);
            }
        } catch (error) { // если во время обновления токена ловим ошибку - ставим isAuthorized == false
            console.log(error);
            setIsAuthorized(false);
        }
    };

    const auth = async () => {                          // проверка обновлён ли токен 
        const token = localStorage.getItem(ACCESS_TOKEN);

        if (!token) { // если нет токена - возвращаем фолс
            setIsAuthorized(false)
            return
        }

        const decoded = jwtDecode(token);
        const tokenExpiration = decoded.exp;
        const now = Date.now() / 1000;

        if (tokenExpiration < now) {  // если токен не действителен вызываем функцию refreshToken, если нет - isAuthorized == true
            await refreshToken()
        } else {
            setIsAuthorized(true);
        }
    }

    if (isAuthorized === null) { // пока useState равен  null возвращаем див с загрузкой
        return <div>Loading...</div>
    }

    return isAuthorized ? children : <Navigate to="/login" /> // если isAuthorized = true показываем чилдрен папку если нет - перенапрвление на логин
};

export default ProtectedRoute