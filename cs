/* Общие стили страницы */
body {
    font-family: Arial, sans-serif;
    padding: 30px;
    background-color: #f4f4f4;
    color: #333;
}

.main-title {
    text-align: center;
    color: #000;
}

h2 {
    color: blue;
    font-weight: normal;
    text-decoration: underline;
    margin-top: 30px;
}

/* Контейнеры для заданий (пунктирная рамка как в ворде) */
.task-container {
    border: 1px dotted #000;
    padding: 15px;
    background-color: #fff;
    width: fit-content;
    min-width: 500px;
}

/* Позиционирование */
.flex-row {
    display: flex;
    gap: 15px;
    align-items: flex-start;
}

.inline {
    display: inline-block;
    margin-left: 10px;
}

.mt-10 {
    margin-top: 10px;
}

/* Элементы форм */
input, textarea, select {
    display: block;
    margin-bottom: 10px;
}

input[type="radio"], input[type="checkbox"] {
    display: inline-block;
    margin-bottom: 0;
}

/* Стили из 5-го задания (красные рамки вокруг текста) */
.border-label {
    border: 1px solid red;
    padding: 1px 3px;
    cursor: pointer;
}

.radio-box {
    border: 1px solid #666;
    padding: 10px;
    margin-bottom: 10px;
}

/* Настройки resize (6-е задание) */
.res-limit {
    width: 200px;
    height: 80px;
    max-width: 300px;
    max-height: 150px;
}

.res-none {
    resize: none;
}

.res-vert {
    resize: vertical;
}

.res-hor {
    resize: horizontal;
}
