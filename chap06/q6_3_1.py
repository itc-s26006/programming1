class Nigiri:
       category ="にぎり"
       top="ねた"
       base ="しゃり"
   class Katsuo(Nigiri):
     top="カツオ"
     topping="生姜とねぎ"
       price=100
  def show_attributes(self):
      super().show_attributes()
      print("topping:{}".format(self.topping)) 
 12 k1= Katsuo()
 13 k1.show_attributes()                               
