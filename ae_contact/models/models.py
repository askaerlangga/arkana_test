from odoo import models, fields, api
import requests

class ResPartner(models.Model):
    _inherit = 'res.partner'

    pokemon_url = fields.Char('Url', readonly=True)
    base_hp = fields.Integer('HP')
    base_attack = fields.Integer('Attack')
    base_defense = fields.Integer('Defense')
    base_special_attack = fields.Integer('Special Attack')
    base_special_defense = fields.Integer('Special Defense')
    base_speed = fields.Integer('Speed')
    pokemon_type_ids = fields.Many2many('pokemon.types', string='Pokemon Types')

    def fetch_pokemon_action(self):
        url = "https://pokeapi.co/api/v2/pokemon"
        data = []
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
            else:
                response.raise_for_status()
        except requests.RequestException as e:
            print(f'Failed get pokemon data : {e}')
        
        if data:
            for pokemon in data['results']:
                partner = self.env['res.partner']
                available = partner.search([('name','=',pokemon['name'])])
                if not available:
                    res = partner.create({
                        'name': pokemon['name'],
                        'pokemon_url': pokemon['url'],
                    })
                    print(f'{res.name} created')
                else:
                    print(f'{available.name} is available')

    def fetch_pokemon_detail_action(self):
        for rec in self:
            if rec.pokemon_url:
                data = []
                try:
                    response = requests.get(rec.pokemon_url)
                    if response.status_code == 200:
                        data = response.json()
                    else:
                        response.raise_for_status()
                except requests.RequestException as e:
                    print(f'Failed get pokemon data : {e}')

                if data:
                    rec.base_hp = data['stats'][0]['base_stat']
                    rec.base_attack = data['stats'][1]['base_stat']
                    rec.base_defense = data['stats'][2]['base_stat']
                    rec.base_special_attack = data['stats'][3]['base_stat']
                    rec.base_special_defense = data['stats'][4]['base_stat']
                    rec.base_speed = data['stats'][5]['base_stat']

                    pokemon_types = []
                    for types in data['types']:
                        available = self.env['pokemon.types'].search([('name','=', types['type']['name'])])
                        if not available:
                            res = available.create({
                                'name' : types['type']['name'],
                                'url' : types['type']['url']
                            })
                            pokemon_types.append(res.id)
                        else:
                            pokemon_types.append(available.id)
                    rec.pokemon_type_ids = [(6, 0, pokemon_types)]

class PokemonTypes(models.Model):
    _name = 'pokemon.types'

    name = fields.Char('Name')
    url = fields.Char('Url')