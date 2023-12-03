from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
import os

class CartaPokemon(BoxLayout):
    def __init__(self, nome, tipo_pokemon, habilidades, hp, ataque, defesa, velocidade, total, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint = (None, None)
        self.size = (600, 200)

        self.imagem = Image(source=os.path.join("imagens", f"{nome.lower()}.png"), size_hint=(None, None), size=(200, 200))

        self.layout_status = BoxLayout(orientation='vertical', spacing=5)
        self.label_nome = Label(text=nome, size_hint_y=None, height=30, halign='center')
        self.label_tipo = Label(text=tipo_pokemon, size_hint_y=None, height=30, halign='center')
        self.label_status = Label(
            text=f'Status\nHP: {hp}\nAtaque: {ataque}\nDefesa: {defesa}\nVelocidade: {velocidade}\nTotal: {total}',
            halign='center', size_hint_y=None, height=80
        )
        self.layout_status.add_widget(self.label_nome)
        self.layout_status.add_widget(self.label_tipo)
        self.layout_status.add_widget(self.label_status)

        texto_habilidades = "\n".join(habilidades)
        self.label_habilidades = Label(
            text=f'Habilidades\n{texto_habilidades}', valign='middle', halign='left'
        )

        self.add_widget(self.imagem)
        self.add_widget(self.layout_status)
        self.add_widget(self.label_habilidades)

class AppPokedex(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=10)

        self.search_input = TextInput(hint_text='Pesquisar por nome de Pokémon', multiline=False, size_hint_y=None, height=40)
        self.search_input.bind(text=self.on_search_text_change)
        
        self.layout.add_widget(self.search_input)

        self.scrollview = ScrollView()
        self.grid_layout = GridLayout(cols=1, spacing=20, size_hint_y=None)

        self.pokemons = [
            {"nome": "Pikachu", "tipo_pokemon": "Tipo: Elétrico", "habilidades": ["*Choque do trovão", "*Investida elétrica"],
             "hp": 150, "ataque": 35, "defesa": 150, "velocidade": 300, "total": 635},
            {"nome": "Bulbasaur", "tipo_pokemon": "Tipo: Grama", "habilidades": ["*Chicote de cipó", "*Folha navalha"],
             "hp": 200, "ataque": 50, "defesa": 250, "velocidade": 200, "total": 700},
            {"nome": "Charmander", "tipo_pokemon": "Tipo: Fogo", "habilidades": ["*Lança-chamas", "*Bola de fogo"],
             "hp": 100, "ataque": 95, "defesa": 200, "velocidade": 250, "total": 645},
            {"nome": "Squirtle", "tipo_pokemon": "Tipo: Água", "habilidades": ["*Jato de água", "*Cascata"],
             "hp": 250, "ataque": 65, "defesa": 300, "velocidade": 150, "total": 765},
            {"nome": "Venusaur", "tipo_pokemon": "Tipo: Planta/Venenoso", "habilidades": ["*Raio solar", "*Folha navalha"],
             "hp": 600, "ataque": 650, "defesa": 650, "velocidade": 450, "total": 2350},
            {"nome": "Charizard", "tipo_pokemon": "Tipo: Fogo/Voador", "habilidades": ["*Lança-chamas", "*Giro de fogo"],
             "hp": 550, "ataque": 700, "defesa": 600, "velocidade": 500, "total": 2350},
            {"nome": "Blastoise", "tipo_pokemon": "Tipo: Água", "habilidades": ["*Jato de água", "*Surf"],
             "hp": 600, "ataque": 650, "defesa": 800, "velocidade": 450, "total": 2500}
        ]

        for dados_pokemon in self.pokemons:
            carta_pokemon = CartaPokemon(**dados_pokemon)
            self.grid_layout.add_widget(carta_pokemon)

        self.grid_layout.bind(minimum_height=self.grid_layout.setter('height'))
        self.scrollview.add_widget(self.grid_layout)
        self.layout.add_widget(self.scrollview)

        return self.layout
    
    def on_search_text_change(self, instance, value):
        filtered_pokemons = [pokemon for pokemon in self.pokemons if value.lower() in pokemon['nome'].lower()]
        self.grid_layout.clear_widgets()
        
        for dados_pokemon in filtered_pokemons:
            carta_pokemon = CartaPokemon(**dados_pokemon)
            self.grid_layout.add_widget(carta_pokemon)

if __name__ == '__main__':
    app = AppPokedex()
    app.run()






