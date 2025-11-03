import React, { useEffect, useState } from 'react';
import './Header.css';
import axios from 'axios';

const Header = () => {
    const [menuItems, setMenuItems] = useState([]);
    // Убираем завершающий слеш если есть
    const API_URL = (process.env.REACT_APP_API_URL || 'http://localhost:8000/api').replace(/\/$/, '');

    useEffect(() => {
        axios.get(`${API_URL}/menu/`)
            .then(response => {
                // Проверяем, что response.data является массивом
                if (Array.isArray(response.data)) {
                    setMenuItems(response.data);
                } else {
                    console.error('Menu items is not an array:', response.data);
                    setMenuItems([]);
                }
            })
            .catch(error => {
                console.error('Error fetching menu:', error);
                setMenuItems([]); // Устанавливаем пустой массив при ошибке
            });
    }, []); // eslint-disable-line react-hooks/exhaustive-deps

    return (
        <header className="header">
            <div className="header-container">
                <div className="logo">
                    <span className="logo-text">SPACE<span className="logo-x">X</span></span>
                </div>
                <nav className="nav">
                    <ul className="nav-list">
                        {Array.isArray(menuItems) && menuItems.length > 0 ? (
                            menuItems.map(item => (
                                <li key={item.id} className="nav-item">
                                    <a href={item.url || '#'} className="nav-link">
                                        {item.title}
                                    </a>
                                </li>
                            ))
                        ) : (
                            <li className="nav-item">
                                <span className="nav-link">Загрузка...</span>
                            </li>
                        )}
                    </ul>
                </nav>
            </div>
        </header>
    );
};

export default Header;