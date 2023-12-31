from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.audio import SoundLoader



class soggy_clicker(App):
    def build(self):
        self.soggybucks = 0
        self.soggybuckadd = 1
        self.item1bought = 0
        self.item2bought = 0
        self.item3bought = 0
        self.item4bought = 0
        self.item5bought = 0
       
        self.sogsound = SoundLoader.load('sogsong.mp3')
        #if self.sogsound:
            #self.sogsound.play()
            #self.sogsound.loop = True
        self.victory = SoundLoader.load('victory.mp3')
        
        ##WARNING SCREEN##
        self.warning = Label(text='WARNING!',
                             color = 'red',
                             font_size = 75)
        self.warning.pos = (0, 300)
        self.warning2 = Label(text = 'You are playing an incomplete version of Soggy Clicker.',
                              font_size = 25)
        self.warning2.pos = (0, 150)
        self.warning3 = Label(text = 'Some things may be subject to change in the future.',
                              font_size = 25)
        self.warning3.pos = (0, 75)
        self.warningbtn = Button(text = 'I Understand',
                                 font_size = 50,
                                 size_hint = (1,.2))
        self.warningbtn.pos = (0,0)
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

        self.item1 = Button(text = 'extra sog | cost: 100',
                       font_size = 25,
                       size_hint = (.33, .33))
        self.item1.pos = (0, 604)

        self.item2 = Button(text= 'wetter water | cost: 500',
                            font_size = 25,
                            size_hint = (.33,.33))
        self.item2.pos = (394, 604)

        self.item3 = Button(text = 'golden bath tub | cost: 2000',
                            font_size = 25,
                            size_hint = (.33,.33))
        self.item3.pos = (788, 604)
        
        self.item4 = Button(text='the soggiest cat | cost: 10000',
                            font_size = 25,
                            size_hint = (.33,.33))
        self.item4.pos = (0,308)
        self.next = Button(text = 'nothing to be seen here',
                           size_hint = (.5,.2),
                           font_size = 50)
        self.next.pos = (600, 0)

        self.beatgame = Button(text = 'BEAT GAME! | cost : 20000',
                              
                                font_size = 35,
                                size_hint = (.33,.33) )
        self.beatgame.pos = (394,308)

        ##END SCREEN##
        self.congration = Label(text='congratulations!',
                                font_size = 75,
                                color = 'green')
        self.congration.pos = (0, 300)
        self.youbeat = Label(text= 'You beat Soggy clicker!',
                             font_size = 50)
        self.youbeat.pos = (0,150)
        self.goout = Label(text = 'now go outside...',
                           )    
        self.goout.pos = (0,100)
        
        self.close = Label(text = 'Please close the game when you are ready.',
                           font_size = 35)
       
        
        self.thanks = Label(text = 'Thank you!',
                            font_size = 75,
                            color = 'lime')
        self.thanks.pos = (0,-300)

        ##ADD STUFF##
        self.layout.add_widget (self.warning)
        
        self.layout.add_widget (self.warning2)
        self.layout.add_widget (self.warning3)
        
        self.layout.add_widget (self.warningbtn)
        self.soggycat.bind(on_press = self.soggybuck)
        self.quit.bind(on_release = self.end)
        self.shop.bind(on_press = self.shopbtn)
       
        self.back1.bind(on_press = self.backone)
        self.credits.bind(on_press = self.creditsbtn)
        self.item1.bind(on_release = self.item1buy)
        self.item2.bind(on_release = self.item2buy)
        self.item3.bind(on_release = self.item3buy)
        self.item4.bind(on_release = self.item4buy)
        self.warningbtn.bind(on_release=self.understand)
        self.beatgame.bind(on_release=self.item5buy)
        
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
        self.layout.remove_widget (self.beatgame)
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
         if self.soggybucks >= 2000 and self.item3bought == 0:
            self.item3.text = '[BOUGHT]'
            self.item3.color = 'green'
            self.item3bought = 1
            self.soggybucks = self.soggybucks - 2000
            self.bucks.text = (str(self.soggybucks)+' soggybucks')
            self.soggybuckadd *= 2
    def item4buy(self,btn):
        if self.soggybucks >= 10000 and self.item4bought == 0:
            self.item4.text = '[BOUGHT]'
            self.item4.color = 'green'
            self.item4bought = 1
            self.soggybucks = self.soggybucks - 10000
            self.bucks.text = (str(self.soggybucks)+' soggybucks')
            self.soggybuckadd *= 2
    def item5buy(self,btn):
        if self.soggybucks >= 20000 and self.item5bought == 0:
            self.layout.remove_widget (self.item2)
            self.layout.remove_widget (self.next)
            self.layout.remove_widget (self.item1)
            self.layout.remove_widget (self.item3)
            self.layout.remove_widget (self.item4)
            self.layout.remove_widget (self.beatgame)
            self.layout.remove_widget (self.back1)
            self.layout.add_widget (self.congration)
            self.layout.add_widget (self.youbeat)
            self.layout.add_widget (self.goout)
            self.layout.add_widget (self.close)
            
            self.layout.add_widget (self.thanks)
            if self.sogsound:
                self.sogsound.loop = False
                self.sogsound.stop()
            if self.victory:
                self.victory.play()
            
    def understand(self,btn):
        self.layout.remove_widget (self.warning)
        self.layout.remove_widget (self.warning2)
        self.layout.remove_widget(self.warning3)
        self.layout.remove_widget (self.warningbtn) 
        self.layout.add_widget (self.quit)
        self.layout.add_widget (self.credits)
        self.layout.add_widget (self.welcome)
        self.layout.add_widget(self.shop)
        self.layout.add_widget(self.soggycat)
        self.layout.add_widget(self.bucks)
        if self.sogsound:
            self.sogsound.play()
            self.sogsound.loop = True
       
            

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
        self.layout.add_widget (self.beatgame)
   
        
    
soggy_clicker().run()
