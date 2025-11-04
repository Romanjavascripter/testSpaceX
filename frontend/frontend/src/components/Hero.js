import React, { useEffect, useState } from 'react';
import './Hero.css';
import axios from 'axios';

// Используем переменную окружения или fallback на localhost (БЕЗ завершающего слеша)
const API_URL = (process.env.REACT_APP_API_URL || 'http://localhost:8000/api').replace(/\/$/, '');

const Hero = () => {
    const [heroContent, setHeroContent] = useState({
        main_title: 'ПУТЕШЕСТВИЕ',
        title_highlight: 'ВИЕ',
        subtitle: 'на красную планету',
        button_text: 'Начать путешествие',
        button_url: '#'
    });
    const [advantages, setAdvantages] = useState([]);

    useEffect(() => {
        axios.get(`${API_URL}/hero/`)
            .then(response => {
                // Проверяем что это не HTML страница
                if (response.data && typeof response.data === 'object' && !response.data.toString().includes('<!doctype')) {
                    setHeroContent(response.data);
                }
            })
            .catch(error => {
                console.error('Error fetching hero content:', error);
            });

        axios.get(`${API_URL}/advantages/`)
            .then(response => {
                // Проверяем, что response.data является массивом и не HTML
                if (Array.isArray(response.data)) {
                    setAdvantages(response.data);
                } else {
                    console.error('Advantages is not an array:', response.data);
                    setAdvantages([]);
                }
            })
            .catch(error => {
                console.error('Error fetching advantages:', error);
                setAdvantages([]);
            });
    }, []); // eslint-disable-line react-hooks/exhaustive-deps

    // Защита от undefined
    const mainTitle = heroContent?.main_title || 'ПУТЕШЕСТВИЕ';
    const titleHighlight = heroContent?.title_highlight || 'ВИЕ';
    const mainTitleParts = mainTitle.split(titleHighlight);

    const bgUrl = heroContent?.background_image_url || '/image/mars-clean-bg.jpg';

    return (
        <section className="hero">
            <div 
                className="hero-background"
                style={{
                    backgroundImage: `url('${bgUrl}')`
                }}
            >
                <div className="hero-overlay"></div>
            </div>
            
            <div className="hero-content">
                <div className="hero-left">
                    <h1 className="hero-title">
                        {mainTitleParts[0]}
                        <span className="hero-title-highlight">{titleHighlight}</span>
                        {mainTitleParts[1] || ''}
                    </h1>
                    <p className="hero-subtitle">{heroContent?.subtitle || 'на красную планету'}</p>
                    <a href={heroContent?.button_url || '#'} className="hero-button">
                        {heroContent?.button_text || 'Начать путешествие'}
                    </a>
                </div>
                
                <div className="hero-right">
                    {Array.isArray(advantages) && advantages.length > 0 ? (
                        advantages.map((advantage, index) => (
                            <div key={advantage.id} className="advantage-block" style={{ animationDelay: `${index * 0.1}s` }}>
                                <div className="advantage-title">{advantage.title}</div>
                                <div className="advantage-value">{advantage.value}</div>
                                <div className="advantage-description">{advantage.description}</div>
                            </div>
                        ))
                    ) : (
                        <div className="advantage-block">
                            <div className="advantage-title">Загрузка...</div>
                        </div>
                    )}
                </div>
            </div>
        </section>
    );
};

export default Hero;