# Представлено решение задачи на языке Python3.9
## Задача:
Есть кусочно заданная линейная функция. Функция задаётся точками (x,y), которые соединяются прямыми.

Необходимо получать значение этой функции при определённом значении x.

Так же оценить сложность алгоритма вычисления значения функции в нотации О-большое. Реализация на любом удобном языке, без использования библиотек.

Пример использования реализации:

- Эта кусочно линейная функция заданная двумя точками
- Точки с одинаковым х переписывают друг друга

Входящие точки: x=0,y=100 и x=10,y=122
```python
F = piecewise_func(0,100)(10,122) #.. и т.д
```
 Добавим еще одну точку, к примеру, x=30, y=0
```python
F = F(30, 0)
```
 Вычислим значение от x = 5
```python
F.y(5) 
```
 Результат: 
```python
y = 111
```
# Дополнительная задача. 
Реализовать функцию получения таблицы.

Необходимо получить таблицу вида:

```
--------------------
| x1 | x2 | a | b |
--------------------
|    |    |   |   |
--------------------
|    |    |   |   |
```
Где x1, x2 - это *границы интервала*, a и b - *коэффициенты линейной функции*.
