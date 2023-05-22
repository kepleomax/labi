import tkinter as tk

class Restaurant:

  def __init__(self, restaurant_name, cuisine_type):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type

  def describe_restaurant(self):
    print(f"Название ресторана: {self.restaurant_name}")
    print(f"Тип кухни: {self.cuisine_type}")

  def open_restaurant(self):
    print(f"Ресторан {self.restaurant_name} открыт!")

  '''
  newRestaurant = Restaurant("Persona Grata", "Европейская")
  newRestaurant.describe_restaurant()
  newRestaurant.open_restaurant()
  '''

def z1():

  class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
      super().__init__(restaurant_name, cuisine_type)
      self.flavors = flavors

    def list_flavors(self):
      print("Список доступных сортов мороженого:", ", ".join(self.flavors))

  newIceCreamStand = IceCreamStand("IceIceBaby", "Десерты (мороженое)", ["ванильное", "клубничное", "шоколадное"])

  newIceCreamStand.describe_restaurant()
  newIceCreamStand.open_restaurant()
  newIceCreamStand.list_flavors()
z1()
def z2():
  class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors, location, work_time):
      super().__init__(restaurant_name, cuisine_type)
      self.flavors = flavors
      self.location = location
      self.work_time = work_time

    def list_flavors(self):
      print("Список доступных сортов мороженого:", ", ".join(self.flavors))

    def add_flavor(self, flavor):
      self.flavors.append(flavor)

    def remove_flavor(self, flavor):
      self.flavors.remove(flavor)

    def check_flavor(self, flavor):
      if flavor in self.flavors:
        print(f"Сорт {flavor} доступен в меню")
      else:
        print(f"Сорта {flavor} нет в меню")

    class Popsicle:
      def __init__(self, flavors_popsicle):
        self.flavors_popsicle = flavors_popsicle

      def list_popsicle(self):
        print("Список доступных сортов мороженого на палочке:", ", ".join(self.flavors_popsicle))

      def add_flavor_popsicle(self, flavor):
        self.flavors_popsicle.append(flavor)

      def remove_flavor_popsicle(self, flavor):
        self.flavors_popsicle.remove(flavor)

      def check_flavor_popsicle(self, flavor):
        if flavor in self.flavors_popsicle:
          print(f"Сорт {flavor} доступен в меню")
        else:
          print(f"Сорта {flavor} нет в меню")

    class SoftIceCream:
      def __init__(self, size):
        self.size = size

      def list_soft(self):
        print("Список размеров доступных сортов мягкого мороженого:", ", ".join(self.size))

      def add_size(self, flavor):
        self.size.append(flavor)

      def remove_size(self, flavor):
        self.size.remove(flavor)

      def check_flavor_popsicle(self, flavor):
        if flavor in self.size:
          print(f"Размер {flavor} доступен в меню")
        else:
          print(f"Размера {flavor} нет в меню")

  icecream = IceCreamStand('IceIceBaby', 'Десерты (мороженое)', ['ванильное', 'клубничное', 'шоколадное'], 'ул. Какая-то, 10', 'с 9:00 до 23:00')
  print(f'Где мы находимся: {icecream.location}')
  print(f'Режим работы: {icecream.work_time}')
  icecream.describe_restaurant()
  icecream.open_restaurant()
  print()
  icecream.list_flavors()
  icecream.add_flavor(input('Введите сорт мороженого, для добавления в список: '))
  print()
  icecream.list_flavors()
  icecream.remove_flavor(input('Введите сорт мороженого, для удаления из списка: '))
  print()
  icecream.list_flavors()
  icecream.check_flavor(input('Введите сорт мороженого для проверки наличия: '))
  print()
  icecream.check_flavor(input('Введите сорт мороженого для проверки наличия: '))
  print()

  newpopsicle = icecream.Popsicle(['киви', 'яблоко', 'вишня'])
  newpopsicle.list_popsicle()
  newpopsicle.add_flavor_popsicle(input('Введите сорт мороженого на палочке, для добавления в список: '))
  print()
  newpopsicle.list_popsicle()
  newpopsicle.remove_flavor_popsicle(input('Введите сорт мороженого на палочке, для удаления из списка: '))
  print()
  newpopsicle.list_popsicle()
  newpopsicle.check_flavor_popsicle(input('Введите сорт мороженого на палочке для проверки наличия: '))
  print()
  newpopsicle.check_flavor_popsicle(input('Введите сорт мороженого на палочке для проверки наличия: '))
  print()

  softicecream = icecream.SoftIceCream(['маленькое', 'среднее', 'большое'])
  softicecream.list_soft()
  softicecream.add_size(input('Введите размер мягкого мороженого мороженого на палочке, для добавления в список: '))
  print()
  softicecream.list_soft()
  softicecream.remove_size(input('Введите размер мягкого мороженого мороженого на палочке, для удаления из списка: '))
  print()
  softicecream.list_soft()
  softicecream.check_flavor_popsicle(input('Введите размер мягкого мороженого для проверки наличия: '))
  print()
  softicecream.check_flavor_popsicle(input('Введите размер мягкого мороженого для проверки наличия: '))
  print()
z2()


def z3():
    class IceCreamStand:
      def __init__(self, flavors):
        self.flavors = flavors
        self.selected_flavors = []

        self.root = tk.Tk()
        self.root.title("Ice Cream Stand")

        self.flavors_label = tk.Label(self.root, text="Available Flavors:")
        self.flavors_label.grid(row=1)

        self.flavors_listbox = tk.Listbox(self.root)
        for flavor in self.flavors:
          self.flavors_listbox.insert(tk.END, flavor)
        self.flavors_listbox.grid(row=2)

        self.root.mainloop()

    if __name__ == '__main__':
      flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint"]
      ice_cream_stand = IceCreamStand(flavors)

z3()

