# sys_tool.py — сценарій тільки для прямого запуску

```
>>> py .\src\sys_tool.py
командна строка
```

# click_tool.py — утиліта на click

```
>>> py .\src\click_tool.py --name Alice
Привіт, Alice!
```
```
>>> py .\src\click_tool.py -n peter
Ім’я не підходить
```

# fire_expose.py — «експорт» існуючих методів через fire

```
>>> py src/fire_expose.py greet Alice
Hello, Alice!
```

```
>>> py src/fire_expose.py goodbye Bob
Goodbye, Bob!
```