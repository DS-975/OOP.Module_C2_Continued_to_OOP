# C2.5. "Удобства" при создании классов 17.10.2023

# Создание классов - обычное дело в рамках ООП. Задачи, возникающие
# вокург этого процесса, также довольно типичны. Поэтому синтаксис Python
# предоставляет большое число дополнительных инструментов и
# "улучшений", которые помогают в этом процессе или делают код более
# ясным, понятным, говорящим.

# Один из таких инструментов это специальные декораторы:
# @staticmethod, @classmethod, @property. Их мы сейчас и рассмотрим.

# Декоратор @staticmethod

# В преведущем материале мы говорили об обычных методах класса -
# методах, выполнение которых завязано на конкретный объект класса.
# Традиционно, помимо обычных методов, языки программирования
# поддерживают так называемые статическим методом.

# Статический методы - методы, которые не привязаня к конкретному
#                      отбъекту класса и являются общими для всего класса.

# Например:

class StaticSlass:
# метод bar не содержит элемента self, поэтому является статическим
	def bar():
		print("bar")
		
StaticClass.bar()

# В результате работы выводится сообщение в консоли

# bar

# Можно заметить несколько отличительных особенностей статических
# методов от обычных методов:

# 1. Отсутствие параметра self.

# 2. Вызов не через объект класса, а через класс непосредственно.

# 3. В случае вызова метода от конкретного объекта, будет выдана ошибка, 
#     что метод bar() не принимает аргументов, но какой - то один аргумент
#     ему был передан, а именно self.

sm = StaticClass()
sm.bar()

# TypeError: bar() takes 0 positional arguments but 1 was given

# Декоратор @staticmethod позволяет убрать ошибку из пункта 3. Если мы
# добавим этот декоратор к объявлению метода, то при вызове метода из
# объекта ошибки не произойдёт.

class StaticClass:
	
	@staticmethod #поместили метод декоратором
	def bar():
		print("bar")
		
StaticClass.bar() #вызов метода от класса

sm = StaticClass() #вызов метода из объекта
sm.bar()

# С выводом:
# bar
# bar

# Как вы могли заметить, статические методы можно и не располагать в
# каком - либо классе, а просто ограничеть созданием метода bar() где -
# либо в программе. Сентатически мы бы ничего не потеряли от этого и не
# получили никаких преимуществ производительности или ещё каких - то
# других. Однако существуют так методы, которые хотя и могут быть и
# привязаны к какому - то конкретному объекту, но очень сильно логически
# привязаны к какому - либо классу.

# Например, в классе Dir (папка на компьютере) может быть метод
# separator(), который возвращает разделитель между именнами папок и
# файлов в пути к файлу.

# В пути С:\\temp\test.txt на Windows разделитель \, а в пути
# /tmp/test.txt  на Linux разделитель /, который используется для
# формирования пути к файлу или папке.

# Метод separator() не связан с какими-либо данными объекта, а является
# неким умолчанием для конкретной операционной сиситемы, поэтому в
# данном случае его можно сделать статическим. Иногда такие методы
# помещают в качестве статических в какой-либо класс, просто для того,
# чтобы не создавать странный длинный именнований вроде
# StaticClass.bar(), а создают статический метод bar() внутри класса
# StaticClass.

# Все понимают, что этот метод имеет тесную связь с логикой использования
# класса, при этом не привязан к объктам.

# Когда нужно использовать стаические методы? Хороший вопрос!

# Статические методы надо использовать, когда мы должны выполнить
# какое-то действие, которое не зависит от сосотояния объекта. Например,
# прочитать файл или вывести на экран какую-либо информацию. Иногда
# через стаические методы удобно хранить константы.

class StaticClass:

	@staticmethod
	def GET_BAR(): # вспомним, что константа пишется со всеми заглавными бцквами (капсон)
		return "bar"

print(StaticClass.GET_BAR())

# В результате увидем в консоли:

# bar

# Хотя тут можно было бы обойтись и полями.

# Другое возможное использование - в методах классов фабрик.

# Фабрика (один из шаблонов ООП) - класс, который создаёт
#                                  объекты других классов.

class FiguresFactory:
	@staticmethod
	def createFugure(type, bounding_rect):
		if type == Square:
# create square object
		if type == Elipse:
# create elipse object
# ...
			
# В любов случае статические методв и @staticmethod - скорее
# синтаксический приём, а не функцмональный. Он нужен для более ясного
# именования методов, разделения их модулям и лучшей читемости кода.

# 2.5.1

# 2.5.2

# Статические методы помечаются декоратором...

# @staticmethod

# 2.5.3

# Выберите верные утверждения:

# 1. Статические методы можно вызывать без обращения к классу.

# 2. Статические методы используются только для хранения данных
#     общих для всех классов.

# 3. Статические методы используются для выполнения
#     определённых процедур, общих для любого объекта класса. +++

# 4. Через статические методы нельзя получить информацию об объекте. +++

# 5. Статические методы - это методы статических объектов.

# 6. Статические методы можно вызывать и через класс, и через объект. +++

# 2.5.4

# Напишите класс SquareFactory с одним статическим методом,
# SquareFactoryпринимающим единственный аргумент - строку квадрат. Данный
# метод должен возвращать объект класса Square с переданной стороной.

# Ответ

class SquareFactory:
	
	@staticmethod
	def create_square(side):
		return Square(side)
		
#Декоратор @classmethod

#Декоратор @classmethod используется для реализации и явного
#обозначения полиморфизма (вспоминаем 15 модель). Напомним,
#полиформизм - это разное поведение методов класса родителя в классе
#наследниках.

#Особенность декоратора @classmethod -первым аргументов в 
#помеченных им методах является модель класса (т.е. объект, который
#представляет сам класс, а не его экземпляр.

#Пример кода:

class ParentClass:
	
	#метод, помещённый @classmethod - первый аргумент cls - модель
	#класса имя которого будет выводиться на печать при вызове
	@classmethod
	def  call_original_method(cls):
		print("%s classmethod. %d" % (cls.__name__, arg))

# этот метод будет заменяться в дочернем классе
		@classmethod
		def call_original_method(cls):
			cls.method(5)

		# это обычный метод
		def call_class_method(self):
			self.method(10)

class ChildClass(ParentClass):

	# метод, заменяющий метод родительского класса
	@classmethod
	def call_original_method(cls):
		cls.method(6)

# Вызываем методы класса через класс.
ParentClass.method(0)  # ParentClassclassmethod. 0
ParentClass.call_original_method()  # ParentClassclassmethod. 5

ChildClass.method(0)  # ChildClassclassmethod. 0
ChildClass.call_original_method()  # ChildClassclassmethod. 6

# Вызываем методы класса через объект.
my_obj = ParentClass()
my_obj.call_class_method()  # ParentClassclassmethod. 10
my_obj.method(1)  # ParentClassclassmethod. 1

# Зачем нужны % по краям classmethod в примере
# print("%s classmethod. %d" % (cls.__name__, arg))?
# Эти операторы представляют собой синтаксис форматирования строк,
# позаимствованный из языка C. %s и %d заменяется тем, что стоит
# после %. Основная разница между ними состоит в том, что %s используется
# как заполнитель для строковых значений, а %d используется как
# заполнитель для целых значений. Более подробно об этом, а также
# про сравнение этих операторов можно прочитать по ссылке:
# Разница между %s и %d в форматировании строк Python

# Метод может вызываться как через ParentClass, так и через ChildClass.
# Только в качестве первого аргумента передаётся не сам объект, а модель
# класса. Как показывает пример кода, декоратор @classmethod имеет смысл
# использовать в тех случаях, когда нужно знание о том, какой класс
# вызывает метод. В реальности это знание нужно нечасто, поэтому и
# применяется декоратор нечасто. Тем не менее в определённой ситуации
# он может сыграть свою роль, поэтому помнить про него стоит.

# Декоратор @property

# Одним из принципов ООП является сокрытие данных. В идеале, пользователь
# вашего класса/подсистемы/системы/программы не должен знать как она
# устроена, а должен пользоваться предоставленным API (Application
# Programming Interface — «программный интерфейс приложения»). Это
# облегчает разработку/доработку, внесение изменений и позволяет
# разделять систему на небольшие части, которые легко реализовать.

# Python, хотя изначально и задумывался как объектно-ориентированный
# язык, тем не менее, и ввиду архитектуры, и факта, что является
# интерпретируемым языком, не претендовал на строгую реализацию ООП
# (в отличие от Java).

# Мы можем увидеть, что при обычном написании классов поля класса,
# которые в ООП, как правило, должны быть скрытыми, в Python остаются
# «на виду». Это иногда может приводить к неверному использованию со
# стороны пользователей класса, например, если мы пишем библиотеку
# или какую-то достаточно сложную систему.

class SomeClass:
	def __init__(self, someData) -> None:
		# мы сохраняем переданные в конструкторе класса данные в поле internalData
		self.internalData = someData


if __name__ == "__main__":
	someObj = SomeClass(5)
	# как видно мы довольно легко можем получить доступ к внутренним данным класса
	# что не слишком-то хорошо
	print(someObj.internalData)

# Декоратор @property позволяет организовывать класс так, чтобы скрыть
# внутреннюю структуру класса от посторонних глаз (насколько это возможно)
# и оставить видимым только нужный API.

# Как это сделать?

# В классе создаются методы, которые выполняют функцию:

# * getter’ов — методов, которые получают значение поля;

# * если нужно, setter’ов — методов, которые устанавливают
#   значения полей, соответствующих тем, что помечены декоратором
#   @property.

# В это время сами поля класса указываются с двойным подчеркиванием
# в начале названия. Это скрывает их, хотя доступ можно получить,
# если указать имя переменной по следующей схеме
# object._classname__privatestuff.

# Пример:

class SomeClass:
	def __init__(self, someData) -> None:
		self.__internalData = someData

	@property
	def data(self):
		return self.__internalData

	@data.setter  # так обозначается сеттер на поле data
	def data(self, value):
		self.__internalData = value


if __name__ == "__main__":
	someObj = SomeClass(5)
	# print(someObj.__internalData) # если мы попытаемся получить доступ к данным напрямую
	# то получим сообщение об ошибке

	print(someObj.data)  # выведет 5

	someObj.data = 10  # всё правильно
	print(someObj.data)  # выведет 10

# Как видите, у пользователя нет доступа к внутренним полям класса,
# а мы создали новое «виртуальное» поле data, которые можно
# использовать как для чтения, так и для записи. Так же можно
# делать поля только для чтения и задавать в качестве полей более
# сложные функции, которые, допустим, выдают некое производное значение.

# Пример:



# класс, который представляет собой значение угла
class Angle:
	def __init__(self, angle = 0) -> None:
		self.__angle = angle

	@property
	def angle(self):
		return self.__angle

	@angle.setter
	def angle(self, angle):
		self.__angle = angle


#свойство, которое возвращает значение угла в радианах
	@property
 	def rad(self):
    return (self.__angle/180.0)*3.14

if __name__ == "__main__":
  	angle = Angle(30)
# выводим значение угла в угловых и радиальных значениях
  	print(f'{angle.angle} : {angle.rad}')

# Вывод:
#
# 30 : 0.4997701026431024


# В представленном классе у нас есть: 1 внутреннее поле
# __angle, которое недоступно пользователю, и 2 внешних:

# * angle — доступное и для чтения, и для записи, которое
#   позволяет работать с углом в градусах.

# * rad — доступное только для чтения, которое позволяет
#   получить значение угла в радианах. При этом если попытаться
#   установить поле rad.



# angle.rad = 0.1

# Будет выдана ошибка:

# AttributeError: can't set attribute

# Декоратор @property полезен — он помогает сделать код более
# ясным, а также позволяет предоставить пользователю тот API,
# которым он должен пользоваться.

# 2.5.5

# Сопоставьте: методы класса, свойства, сеттеры.

# 2.5.6

# Сеттеры помечаются декоратором @свойство. ...

# setter

# 2.5.8

# Создайте вычисляемое свойство для класса Square.

# * Сделайте метод по вычислению площади свойством.

# * Сделайте сторону квадрата свойством, которое можно
#   установить только через сеттер.

# * В сеттере добавьте проверку условия, что сторона должна
#   быть неотрицательной.

#класс, представляющий квадрат
class Square:
    _a = None


    #конструктор с параметром a
    def __init__(self, a):
        if a > 0:
            self._a = a


    #создаем свойство a при помощи декоратора
    @property
    def a(self):
        return self._a


    #указываем сеттер для свойства
    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value


# Best Practices в написании классов

# Давайте подытожим знания о написании классов в Python и
# составим список best practices.

# С архитектурной точки зрения лучшие практики будут звучать так:

# 1. Проанализируйте задачу и выявите обособленные области
#    ответственности. Например, представление данных координат, преобразование данных формата А в формат Б и т.д.

# 2. Поставьте каждой области ответственности определённую
#    сущность (класс). Например, данные координат — класс Point2D,
#    корзина покупателя — класс Chart и т.д.

# 3. Продумайте API для класса:
#     * какие данные и как он будет получать на вход;
#     * какие данные и как он будет отдавать вовне;
#     * какие методы можно будет вызывать извне.

# 4. Распределите классы по модулям (если требуется).


#  практической точки зрения для конкретной реализации
#  классов в Python можно следовать следующим рекомендациям:

# 1 Создавайте все внутренние поля класса в конструкторе,
#   так вы исключите возможность того, что какого-то поля
#   не окажется в нужный момент.



class Miscast:
  def __init__(self) -> None:
      pass

  def setValue(self,value):
     self.value = value

  #если вызвать getValue, до того как было вызвано setValue,
  #возникнет исключение, поскольку поля value до этого отсутствует
  def getValue(self):
     return self.value

if __name__ == "__main__":
  mis = Miscast()
  mis.getValue()

AttributeError: 'Miscast' object has no attribute 'value'

# 2. Делайте различия между общими (теми, которые имеют
#    отношение к самому классу) и частными (те, которые
#    имеют отношение к конкретному объекту) методами класса.
#    Пользуйтесь для этого декоратором @classmethod.

# Пример:

class BankAccount:
	MIN_BALANCE = -10_000

	def __init__(self, owner, account_number, balance=0):
		self.owner = owner
		self.account_number = account_number
		self.created_at = datetime.now().date()

	# общий метод класса, который создает объект прочитывая соответствующий csv файл
	@classmethod
	def from_csv(cls, filepath):
		with open(filepath, "r") as f:
			row = csv.reader(f).__next__()
			owner, account_number = row
		return cls(owner, account_number)


if __name__ == "__main__":
	my_account = BankAccount.from_csv("testfile.csv")
	print(my_account._owner, my_account._account_number, my_account._balance)

# Что записано в MIN_BALANCE?
# Это способ отделять нули в больших числах.
# Питон его считывает как int.
# Примеры можно посмотреть по ссылке:
# What do underscores in a number mean?

# 3. Определяйте операцию сравнения на равенство объектов,
#    когда это имеет смысл, реализуя метод __eq__.

class Angle:
 def __init__(self, angle = 0) -> None:
     self.__angle = angle


 # метод __eq__ позволяет сравнивать объекты, используя оператор ==
 def __eq__(self, __o: object) -> bool:
     return self.__angle == __o.__angle

 @property
 def angle(self):
    return self.__angle

 @angle.setter
 def angle(self, angle):
    self.__angle = angle

if __name__ == "__main__":
  a1 = Angle(30)
  a2 = Angle(45)
  a3 = Angle(30)
  print(f'a1 == a2 -> {a1 == a2}')
  print(f'a1 == a3 -> {a1 == a3}')

# 4. Вывод:

# a1 == a2 -> False
# a1 == a3 -> True

# Другим, похожим на __str__ методом, является метод __repr__.
# Его используют для того, чтобы получить строку создания объекта.

class Angle:
def __init__(self, angle = 0) -> None:
	self.__angle = angle

def __str__(self):
	return f"""Angle: value = {self.__angle}"""

def __repr__(self) -> str:
	return f"""Angle(angle={self.__angle})"""

@property
def angle(self):
	return self.__angle

@angle.setter
def angle(self, angle):
	self.__angle = angle

if __name__ == "__main__":
	a = Angle(30)
	print(a) # выведет Angle: value = 30
	print(repr(a)) #выведет Angle(angle=30)

# Если не реализовать __str__ и __repr__, будет выведено:

# <__main__.Angle object at 0x1005cfe80>
# <__main__.Angle object at 0x1005cfe80>

# Это гораздо менее информативно.

# 5. Оформляйте статические методы при помощи @staticmethod.
#    Это сделает ваш код более читабельным, а вашу идею при
#    создании класса — более явной.

# 6. Помечайте поля и методы:

# * Одно нижнее подчеркивание — для внутреннего использования. “_”
#   ничего не делает, но говорит внешним пользователям класса о
#   том, что это поле или метод для «внутреннего» использования,
#   не рекомендуя их использовать.

# * Два нижних подчеркивания — скрытые. “__” (почти) полностью
#   скрывает поле или метод от посторонних глаз. Сокрытие данных
#   важная часть ООП, не стоит ей пренебрегать.

# 7. Предоставляйте поля во внешний API при помощи декоратора @property.

# 8. Сопровождайте свои методы и классы docstring.

# docstring — краткие описания самих классов, их предназначения и API,
#             которые могут быть вызваны в процессе выполнения
#             при помощи автоматического поля __doc__.

class Angle:
# docstring — краткое описание класса, которое в дальнейшем может быть получено через поле __doc__
"""
   A class used to represent an angle.
   Attributes
   ----------
   angle : int
   rad : int (readonly)

   Methods
   -------
   normalize()
       gets angle value to range from 0 to 360
"""

def __init__(self, angle = 0) -> None:
	self.__angle = angle

@property
def angle(self):
	return self.__angle

@angle.setter
def angle(self, angle):
	self.__angle = angle

@property
def rad(self):
	return (self.__angle/180.0)*math.pi

def normalize(self):
	self.__angle = self.__angle % 360

if __name__ == "__main__":
	print(Angle.__doc__) #вывод на печать описания класса выше

# 9. В реальной практике вы гораздо чаще будете встречаться с
# 	 декоратором @propetry. Декораторы @classmethod и @staticmethod
# 	 нужны в более специфических ситуациях. Даже так: не во всех
# 	 ситуациях они будут уместны. Раз @propetry более ходовой декоратор,
# 	 давайте рассмотрим, как с ним работать, на примере класса
# 	 для пользователя приложения:

#    property_decorator

# Универсального правила использования декораторов,
# перечисленных в юните, нет. Главное, больше практикуйтесь
# в написании кода, и со временем вы будете понимать,
# когда их нужно использовать.

# Все эти рекомендации или «лучшие практики» помогут сделать
# ваши классы не только функциональными, но и красивыми,
# ясными и удобными в использовании. Код, который вы написали,
# сможет вам «помогать», и вы почувствуете гораздо большее
# удовлетворение от того, что делаете :)

