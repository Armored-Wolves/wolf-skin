// здесь реализуется перехватчик запросов, который добавляет автоматически нужные хэдеры ко всем отправляемым ФЕ запросам
import axios from "axios";
import { ACCESS_TOKEN } from "./constants";

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL // обознение BE урл как базового урла
});

// ниже проверка есть ли ACCESS_TOKEN в локал стораж. 
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem(ACCESS_TOKEN);
        if (token) {
            config.headers.Authorization = `Bearer ${token}` // если токен в локал стораж - добавляем его в хэдер
        }
        return config;
    },
    (error) => {
        return Promise.reject(error) // если нет - возвращаем ошибку
    }
);

export default api;