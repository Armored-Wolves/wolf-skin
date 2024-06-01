// форма, в которой решается отображать страницу Логина или Регистрации в зависимости от роутинга
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants";
import api from "../api";
import Registration from "../pages/Registration";

function Form({ route, method }) {
    // создание стейтов для основных переменных и навигейта
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const name = method === "login" ? "Login" : "Registration"; //если метод Логин - отображать страницу логина; если нет - регистрация

    const handleSubmit = async (e) => {
        setLoading(true); // после нажатия на сабмит запускаем индикатор загрузки
        e.preventDefault();

        try {
            const res = await api.post(route, { username, password }) // отправление пост запроса (api === axios.create {baseURL:})... с юзернейм и пасворд
            if (method === "login") {
                localStorage.setItem(ACCESS_TOKEN, res.data.access);
                localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
                navigate("/home")
            } else {
                navigate("/login")
            }
        } catch (error) {
            alert(error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <>
            <form onSubmit={handleSubmit}>
                <h1>{name}</h1>
                <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} placeholder="username"></input>
                <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="password"></input>
                <button type="submit">{name}</button>
            </form>
        </>
    )


}

export default Form;