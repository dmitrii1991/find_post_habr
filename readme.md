# Поиск интерсных постов в обход ограничения в 50 листов Hubra

## При  испольпользовании aiohttp  или  многопотока возникает блокировка с Hubra. Поэтому наслаждаемся одним потоком. (0.5 сек м/у запросами)

> Программа подствавляет значения в адрес последовательно в
*https://habr.com/ru/post/**Номер поста**/*
и выводит совпадение в файл Excel.  

```python
 habr_post(start=430_000, end=429_990, find=['Питон', 'питон', 'Python', 'python'])
```

