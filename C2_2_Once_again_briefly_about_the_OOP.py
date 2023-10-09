# С2.2. Ещё раз коротко про ООП

#Функции 

#Как вы могли убедиться работая с предыдущими модулями, небольшую
#программу или алгоритм возможно написать, не прибегая к каким-либо
#ухищрением. Однако, когда кода становится много *очень много0, и в нём
#появляются повторяющиеся блоки, подпрограммы и подалгоритмы,
#возникает необходимость его структурировать. Тут нам на помощь
#приходят функции.

#Сравните:

#Без использования функциий ↓

streaming = ['netflix', 'hulu', 'desney+', 'appletv+']
	platform1 = 'netflix'
	platform2 =  'hulu'
	
	for i in range(len(streaming)):
		if streaming[i] == platform1:
		
	print("Platform1 is found")
	
	for i in range(len(streaming)):
		if streaming[i] == platform2:
		
	print("Platform1 is found")
	
# С использования функциий ↓

def search(list, platform):
	for i in range(len(streaming)):
		if streaming[i] == platform:
			return True
		return False
		
if __name__ == "__main__":
	streaming = ['netflix', 'hulu', 'desney+', 'appletv+']
	platform1 = 'netflix'
	platform2 =  'hulu'
	
	print(f"Platform1 found: {saerch(streaming, platform1)}")
	print(f"Platform2 found: {saerch(streaming, platform2)}")
	
#Объекты и классы

#Если вы продолжаете писать программы, то сталкиваетесь с тем, что
#возможности стандартных типов (чисел, строк и т.д.) можно исчерпать
#довольно быстро, особенно если описывать объекты и или явления
#реального мира, у которых много различных измерений и свойств.
#Появляется необходимость в агрегаторах. В этой ситуаци нам
#понадобиться объекты и классы, чтобы мы могли работать со множеством
#разрозненных, но логически связанных между собой, свойств. Так нам
#становиться легче определить связанными свойствами, тиражировать и 
#обрабатывать однотипные объекты.

#Давайте рассмотрим, как создать человека двумя способами: сначала без
#использования классов, а затем с их использованием.

#Без использования классов ↓

if __name__ == "main__":
	person1_name = "Max"
	person1_age = 19
	person1_sex = 'M'
	person1_height = 180
	person1_weight = 75
	
	person2_name = "July"
	person2_age = 17
	person2_sex = 'W'
	person2_height = 170
	person2_weight = 60
	
	print(f"person 1: {person1_name}")
	print(f"person 2: {person2_name}")


#С использования классов ↓

class Person:
	def __init__(self, name, age, sex, height, weight) -> None:
		self.name = name
		self.age = age
		self.sex = sex
		self.height = height
		self.weight = weight
		
if __name__ == "__main__":
	person1 = Person("Max", 19, 'M', 180, 75)
	person2 = Person("July", 17, 'W', 170, 60)	
	
	print(f"person 1: {person1_name}")
	print(f"person 2: {person2_name}")
	
#Примечание: Знак -> определяет аннотацию типов. аннотация типов - это
#дополнительное описание в классах, функцях, переменных, которые
#указывает какой тип данных должен быть в этом месте. Это имеет ряд
#преимуществ, например, при создании объектов будут сразу описаны типы
#данных.  

#___________________________________________________
#Разрозненные свойства    |   Свойства, объединённые в класс |
#                    |                      |                              |                          |                 
#                   v                      |                             v                          |
#                                           |                          ___                         |                
#   •          •         •                 |                        /        \                       | 
#      •        •                          |                      /            \                     | 
#•              •          •               |                __/________\__              |     
#   •    •           •                     |                \   |                 |   /              |
#              •         •                 |     •          /   •               •   \              |      
#  •    •        •           •            |               /          class         \             |                
#              •           •               |    •        /     • •  •   •             \           |                    
#    •        •        •                  |              |     • • • • •    •          |          |                                  
#          •          •           •        |   •         \ ______________ /          |          
#    •                  •                  |                                                        |  
# _____________________|___________________________ |              
#                                                                                                   |                                                                                                                                                                                 
#                                                                                                   |                                        
#            object1                      object2                     object3           |                                                                         
#                                                                                                   |                             
#                _ _                           _ _                          _ _               |                                                             
#               /     \                         /     \                        /     \              |                                                                    
#         __/ ____\__             __/ ____\__            __/ ____\__        |                                                                                            
#         \   |          |  /              \   |          |  /             \   |          |  /        |                                                                                 
#         /  • class •  \              /  • class •  \             /  • class •  \        |                                                                             
#       /   • •  •  •      \           /   • •  •  •      \          /   • •  •  •      \      |                                                                                             
#      |    • • • • •   •   |          |   • • • • •   •   |         |    • • • • •   •  |     |                                                                                            
#      \ __________/           \_________ /          \__________/      |                                                                            
#                                                                                                   |
# _________________________________________________|  

#Возможности, которые нам открывают клакссы, оказываются более
#широкими, чем просто объединение нескольких свойств.

#Дополнительные возможности которые мы получаем:

#1 Возможность объединенять классы в иерархии. Это позволяет
#   постепенно наращивать функциональнось и более полно
#   использовать уже написанный код.

#Например, иерархия объектов окружающего мира:

class Obgect:
	def __init__(self, name) -> None:
#Полное name будет представлять в объектах этого класса
#и в объектах всеъ классов наследников
		self.name = name
	
#тоже относиться и к методу getName(),
#который будучи однажды реализован не нужно будет
#уже повторять в дочених классах
	def getName(self):
		return self.name
		
#В классе ФизическийОбъект добавим свойства вес и размер
class PhisicalObdect(Object):
	def __init__(self, name, weight, size) -> None:
		super().__init__(name)
		self.weight = weight
		self.size = size
		
	def getWeight(self):
		return self.weight
		
	def getSize:
		return self.size
		
#классы живых и не живых объектов повторяют все
#поля и методы класса PhisicalObdect (автоматически)
#и используются, чтобы разделить иерархию на две 
#ветви от НеживыхОбъектов можно будет ввести иерархию в
#камни, метал, газы и т.д. , а от живых - в Растения, 
#Животные, Насекомые, Грибф и т.д.

class NonLivingObject(PhisicalObdect):
	def __init__(self, name, weight, size) -> None:
		super().__init__(name, weight, size)
		
class LivingObject(PhisicalObdect):
	def __init__(self, name, weight, size) -> None:
		super().__init__(name, weight, size)
		
#Примечание: мы пишем super().__init__(name, weight, size) потому, что
#заново конструируем класс и берём свойства name из
#родительского, а остальное пишем новое.

#Что означает ->None?
#Возможная иерархия классов                                                                                                                                           
#object                                            ____________________                                                               
#   ├─────┐                              /    _____  person______    \                                               
#living       non-living                    /    /      __   humsn____    \     \                                               
#   ├─────┐                           /    /     /     _ animal__     \    \     \                                             
#animal      plant                        /    /     /     / live_entity \     \    \     \                             
#   │                                        /    /     /     /    /         \     \     \    \     \               
#human                                   |     |     |     |     | object | ─ |  ─ | ─ |  ─ |  ──  Внутри иерархии
#   │                                        \    \     \    \     \____ /     /     /    /     /          количесво свойств  
#person                                     \    \     \    \ ________ /     /    /     /            увеличивается           
#   │                                           \    \     \_____________/    /     /         
#employee                                    \    \_________________/     /                             
#                                                    \_____________________/                     
                                                                                    
#2 Возможность создавать более сложные объекты, объединяя в
#   качестве полей класса не базовые типы, а созданные нами
#   объекты более сложных классов (ИНКАПСУЛЯЦИЯ, помните).

#Например:

class Person:
	def __init__(self, name, age, sex, height, weight) -> None:
		self.name = name
		self.age = age
		self.sex = sex
		self.height = height
		self.weight = weight
		
#класс семья оперирует не объектами базовых типов, 
#а объектами более сложного класса Person.

class Family:
	def _init__(self, familyName) -> None:
		self.members = [] 
		self.familyName = familyName
		
	def addMember(self, person):
		self.members.append(person)
		
if __name_ == "__main__":
	family = Famile("Petrov")
	family.addMember(Person('Petr, 22, 'M', 182, 76))
	
#2.2.1

#Какие поля содержат объект класса LivingObject ?

class Obgect:
	def __init__(self, name) -> None:
#Полное name будет представлять в объектах этого класса
#и в объектах всеъ классов наследников
		self.name = name
	
#тоже относиться и к методу getName(),
#который будучи однажды реализован не нужно будет
#уже повторять в дочених классах
	def getName(self):
		return self.name
		
#В классе ФизическийОбъект добавим свойства вес и размер
class PhisicalObdect(Object):
	def __init__(self, name, weight, size) -> None:
		super().__init__(name)
		self.weight = weight
		self.size = size
		
	def getWeight(self):
		return self.weight
		
	def getSize:
		return self.size
		
#классы живых и не живых объектов повторяют все
#поля и методы класса PhisicalObdect (автоматически)
#и используются, чтобы разделить иерархию на две 
#ветви от НеживыхОбъектов можно будет ввести иерархию в
#камни, метал, газы и т.д. , а от живых - в Растения, 
#Животные, Насекомые, Грибф и т.д.

class NonLivingObject(PhisicalObdect):
	def __init__(self, name, weight, size) -> None:
		super().__init__(name, weight, size)
		
class LivingObject(PhisicalObdect):
	def __init__(self, name, weight, size) -> None:
		super().__init__(name, weight, size)
		
#А у него нет полей 

#В name +++

#C weight +++

#D size +++

#Мы узнали, что, благодаря перечисленным выше свойствам
#(инкапсуляции, наследованию и полиморфизму)б ООП помогает нам
#эффективно использовать код, распределять ответственность по классам
#и "писать меньше, но лучше".

#ООП даёт ясное понимание того, как нужно разбивать задачи на 
#подзадачи, а также позволяет эффективно структурировать код. Никакой
#магии -- ООП  преследует только практические цели:)

#Стоит помнить, что ООП это концепция, а не закон. Есть языки,
#которыем следуют ей более строго (такие, как java, C++ и C#) и менее
#строго (например, JS). Python реализует принципы ООП, но не слишком
#строго. Всё, или почти всё, в Python являеться объектами, к которым
#можно присойдинять любые свойства и методы "на ходу". С одной 
#стороны, это можно пытаться использовать. С другой - это вносит
#хаос и сумятицу в код. Его становится труднее читать и поддерживать,
#потенциально он начинает содержать больше ошибок, как в этом
#примере:

#иллюстрация к возможности присоединять свойства к "чему
#угодно" Python.

#объявление функции 
def someFunc():
#печатаем значение присоединённого свойства к объекту функции,
	print(f'attached property value from gunc itself {someFunc.someAttachedProperty}')
# но откуда оно там возьмётся?

if __name__ == "__main__":
#создали объект функции
	someFuncAsObj = someFunc
#присойдинили к нему свойство со значением
#если мы этого не сделаем, то при работе функции будет
#сгенерирована ошибка
	someFuncAsObj.someAttachedProperty = 5 
#вызвали функцию
	someFuncAsObj() # с начала будет распечатано сообщение из функции
	print(f'value of attached property {someFuncAsObj.someAttachedProperty }')
	
#Очевидно, что такой подход многих сбивал бы с толку и противоречил
#дзен Python, который направлен именно на то, чтобы всё было
#максимально чётко, прозрачно и однозначно.

#Если переписать этот пример на синтекс классов, то всё станет гораздо
#яснее.

class SomeClass:
	def __init__(self, propValue = 0) -> None:
		self.setAttachedProperty = propValue
		
	def setAttachedProperty(self, propValue):
		self.attachedProperty = propValue
		
	def getAttachedProperty(self):
		retrun self.attachedProperty
		
	def printContent(self):
		print(f'attached property value from class {self.attachedProperty}')

if __name__ == "__main__":
	obj = SomeClass(5)
	obj.printContent()
	print(f'value of attached property {obj.getAttachedProperty()}')
	
#Такая организация кода явно говорит о том, что мы хотим сделать, и о том,
#как должен функционировать объекты нашего класса. Благодаря
#устройству Python можно присойдинять свойси=тва и методы к "чему угодно"
#и "на ходу", широко использовать кортежи списки и словари, идти на
#другие ухищрения, но делать этого как раз не нужно. Потому что в Python
#есть специализированные инструменты для кождой задачи, которые лучше
#всего справляються именно с ней. Их и нужно использоваьб. Так, синтасис
#классов специально предназначен для того, чтобы можно было применять
#подходы ООП для решения задач. 

#2.2.2

#Какие цели приследуют ООП?

#повышение модульности +++

#повышение ясности кода +++

#повышение скорости использования кода

#чисто декоративвные функции

#Верно:
#принципы ООП позволяют эффективно делить задачу на методы и классы,
#что повышает ясность и модульность кода. Дополнительные вызовы и 
#структура, требует небольших накладных расходов, поэтому скорость,
#возможно, чуть и снежается, но это мелочи по сравнению с пполучаемыми
#выгодами.

#2.2.3

#Укажите основные элементы ООП:

#инкапсуляция +++

#деление

#наследование +++

#обеспечение

#полиморфизм +++

#Вывад:

#  •  ООП - это можный подход к проектированию и реализации
#                 архитектуры программы.

#  •  Реализация ООП в каждом языке, в том числе Python, имеет свой
#     особенности, которые нужно учитывать.

#  •  Синтаксис, который реализует принципы ООП (создание и
#     взаимодействие классов), направлен на повышение модульности,
#     читаемость кода, гибкости и т.д.

#  •  Если создаваемые вами классы не повышают, а снижают
#     модульность, читаемость, значит что, скорее всего, их придётся в 
#     ближайшием будущим переработать.

#Когда мы говорим про ООП, мы по большей части говорим про
#эффективную архитектуру программы. Как это делать правильно,
#лучше всего и постепенно?


