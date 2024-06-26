# OB04.SOLID-principles
Studying the principles of SOLID and learning to break code into more manageable and flexible components.

## Шаг 1: Создание абстрактного класса для оружия

- Класс Weapon: Это абстрактный класс, который определяет общий интерфейс для всех видов оружия в игре. Каждый конкретный класс оружия должен реализовать метод attack(), который описывает действие данного оружия.

## Шаг 2: Реализация конкретных типов оружия

- Классы Sword, Bow и Staff: Эти классы наследуются от Weapon и реализуют метод attack():
Sword и Bow имеют традиционные атаки, как удар мечом и выстрел из лука.
Staff представляет магическое оружие, добавляя элемент фэнтези в игру.

## Шаг 3: Определение класса бойца

- Класс Fighter:
  - Инициализация: При создании бойца ему можно 
  задать имя и начальный уровень.
  - changeWeapon(): Метод для смены оружия.
  Это позволяет динамически изменять стиль боя 
  бойца в зависимости от ситуации.
  - fight(): Метод для начала боя с монстром. 
  Использует текущее оружие бойца для атаки и выводит результат боя.

## Шаг 4: Создание классов монстров
- Абстрактный класс Monster и его наследники 
Goblin и Dragon:
  - Monster определяет общий метод defeat(), который должен быть реализован в каждом конкретном классе монстра.
  - Goblin и Dragon реализуют метод defeat() с уникальными сообщениями о поражении, что добавляет разнообразие в противников.

## Шаг 5: Реализация боя
- Пример использования созданных классов:
  - Боец выбирает оружие (меч, лук, или посох) с помощью метода changeWeapon().
  - Затем боец начинает бой с монстром (Goblin или Dragon), используя метод fight(). Результат боя зависит от выбранного оружия.

## Принцип открытости/закрытости
Этот принцип достигается за счет использования абстрактных классов и интерфейсов для оружия и монстров. Добавление нового типа оружия или нового монстра не требует изменений в существующих классах бойцов или механизме боя. Это позволяет легко расширять игру, сохраняя при этом её основную функциональность.

Такой подход делает код гибким и удобным для масштабирования, позволяя разработчикам добавлять новые функции без риска нарушения существующего функционала.






