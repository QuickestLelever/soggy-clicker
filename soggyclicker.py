from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.audio import SoundLoader
import time
import schedule


class soggy_clicker(App):
    def build(self):
        self.soggybucks = 0
        self.soggybuckadd = 1
        self.item1bought = 0
        self.item2bought = 0
        self.item3bought = 0
        self.item4bought = 0
        self.sogsound = SoundLoader.load('sogsong.mp3')
        if self.sogsound:
            self.sogsound.play()
            self.sogsound.loop = True
        

        ##NORML SCREEN##
        
    

        self.soggycat = Button(background_normal = 'sog.png',
                               size_hint = (.5,.8),
                               background_down = 'evilsog.png',
                               
                               )
        self.soggycat.pos = (0, 180)

        self.shop = Button(text = 'shop ->',
                           size_hint = (.5,.2)
                           )
        self.shop.pos = (600,530)
        self.welcome = Button(text = 'welcome to soggy clicker',
                              size_hint = (.5,.25),
                              font_size = 50,
                              color = 'cyan',
                              background_down = 'sog.png')
        self.welcome.pos = (600, 710)

        self.quit = Button(text = 'quit',
                           size_hint = (.5,.2),
                           color = 'crimson',
                           )
        self.quit.pos = (600, 178)
        
        self.credits = Button(text = 'credits',
                              size_hint = (.5,.2)
                              )
        self.credits.pos = (600, 351)
        
        
        self.bucks = Label(size_hint = (1,.2),
                           text=('0 soggybucks'),
                          )
        self.layout = FloatLayout()
        

        ##CREDITS SCREEN##


        self.credits2 = Button(text='credits',
                               size_hint = (1, .2),
                               font_size = 50,
                               color = 'cyan'
                               )
        self.credits2.pos = (0, 719)
        
        self.leon = Label( text = 'almost everything: leon',
                          font_size = 35)
        self.leon.pos = (0, 200)
        self.adrian = Label(text = 'items: adrian',
                            font_size = 35)
        self.adrian.pos = (0,0)

        self.jonas = Label(text = 'moral support: soggy cat',
                           font_size = 35)
        self.jonas.pos = (0,-200)

        self.back1 = Button(text = 'back <-',
                            font_size = 50,
                            size_hint = (1, .2))
        self.back1.pos = (0,0)


        ##SHOP SCREEN##

        self.item1 = Button(text = 'placeholder | cost: 100',
                       font_size = 25,
                       size_hint = (.33, .33))
        self.item1.pos = (0, 604)

        self.item2 = Button(text= 'placeholder | cost: 500',
                            font_size = 25,
                            size_hint = (.33,.33))
        self.item2.pos = (394, 604)

        self.item3 = Button(text = 'placeholder | cost: 10000',
                            font_size = 25,
                            size_hint = (.33,.33))
        self.item3.pos = (788, 604)
        
        self.item4 = Button(text='plalceholder | cost: 50000',
                            font_size = 25,
                            size_hint = (.33,.33))
        self.item4.pos = (0,308)
        self.next = Button(text = 'next ->',
                           size_hint = (.5,.2),
                           font_size = 50)
        self.next.pos = (600, 0)
        
        self.layout.add_widget (self.quit)
        self.layout.add_widget (self.credits)
        self.layout.add_widget (self.welcome)
        self.layout.add_widget(self.shop)
        self.layout.add_widget(self.soggycat)
        self.layout.add_widget(self.bucks)
        self.soggycat.bind(on_press = self.soggybuck)
        self.quit.bind(on_release = self.end)
        self.shop.bind(on_press = self.shopbtn)
       
        self.back1.bind(on_press = self.backone)
        self.credits.bind(on_press = self.creditsbtn)
        self.item1.bind(on_release = self.item1buy)
        self.item2.bind(on_release = self.item2buy)
        self.item3.bind(on_release = self.item3buy)
        self.item4.bind(on_release = self.item4buy)
        
        return self.layout
        
    
    def soggybuck(self,btn):
        self.soggybucks = self.soggybucks + self.soggybuckadd
        self.bucks.text = (str(self.soggybucks)+' soggybucks')
    def end(self,btn):
        App.get_running_app().stop()
    def backone(self,btn):
        self.back1.size_hint = (1, .2)
        self.layout.remove_widget (self.item2)
        self.layout.remove_widget (self.next)
        self.layout.remove_widget (self.item1)
        self.layout.remove_widget (self.item3)
        self.layout.remove_widget (self.item4)
        self.layout.remove_widget (self.credits2)
        self.layout.remove_widget (self.leon)
        self.layout.remove_widget (self.adrian)
        self.layout.remove_widget (self.back1)
        self.layout.remove_widget (self.jonas)
        self.layout.add_widget (self.bucks)
        self.layout.add_widget (self.soggycat)
        self.layout.add_widget (self.quit)
        self.layout.add_widget (self.credits)
        self.layout.add_widget (self.welcome)
        self.layout.add_widget (self.shop)
    def creditsbtn(self,btn):
        self.layout.remove_widget (self.bucks)
        self.layout.remove_widget (self.soggycat)
        self.layout.remove_widget (self.quit)
        self.layout.remove_widget (self.credits)
        self.layout.remove_widget (self.welcome)
        self.layout.remove_widget (self.shop)
        self.layout.add_widget (self.credits2)
        self.layout.add_widget (self.leon)
        self.layout.add_widget (self.adrian)
        self.layout.add_widget (self.back1)
        self.layout.add_widget (self.jonas)
    def item1buy(self,btn):
        if self.soggybucks >= 100 and self.item1bought == 0:
            self.item1.text = '[BOUGHT]'
            self.item1.color = 'green'
            self.item1bought = 1
            self.soggybucks = self.soggybucks - 100
            self.bucks.text = (str(self.soggybucks)+' soggybucks')
            self.soggybuckadd *= 2
    def item2buy(self,btn):
         if self.soggybucks >= 500 and self.item2bought == 0:
            self.item2.text = '[BOUGHT]'
            self.item2.color = 'green'
            self.item2bought = 1
            self.soggybucks = self.soggybucks - 500
            self.bucks.text = (str(self.soggybucks)+' soggybucks')
            self.soggybuckadd *= 2
    def item3buy(self,btn):
         if self.soggybucks >= 10000 and self.item3bought == 0:
            self.item3.text = '[BOUGHT]'
            self.item3.color = 'green'
            self.item3bought = 1
            self.soggybucks = self.soggybucks - 10000
            self.bucks.text = (str(self.soggybucks)+' soggybucks')
            self.soggybuckadd *= 2
    def item4buy(self,btn):
        if self.soggybucks >= 50000 and self.item4bought == 0:
            self.item4.text = '[BOUGHT]'
            self.item4.color = 'green'
            self.item4bought = 1
            self.soggybucks = self.soggybucks - 50000
            self.bucks.text = (str(self.soggybucks)+' soggybucks')
            self.soggybuckadd *= 2
    def shopbtn(self,btn):
        self.back1.size_hint = (.5,.2)
        self.layout.remove_widget (self.bucks)
        self.layout.remove_widget (self.soggycat)
        self.layout.remove_widget (self.quit)
        self.layout.remove_widget (self.credits)
        self.layout.remove_widget (self.welcome)
        self.layout.remove_widget (self.shop)
        self.layout.add_widget (self.back1)
        self.layout.add_widget (self.item1)
        self.layout.add_widget (self.next)
        self.layout.add_widget (self.item2)
        self.layout.add_widget (self.item3)
        self.layout.add_widget (self.item4)
    def overtime(self):
        self.soggybucks += 1
        time.sleep(1.0)
        
    
soggy_clicker().run()
