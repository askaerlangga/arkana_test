from odoo import models, fields, api

class PokemonXlsx(models.AbstractModel):
    _name = 'report.ae_contact.pokemon_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, obj):
        sheet = workbook.add_worksheet('Pokemon')

        header_style = workbook.add_format({
            'font_size': 13,
            'bold': True,
            'valign': 'vcenter',
            'align': 'center',
            'text_wrap': True,
            'border' : 1
        })
        text_style = workbook.add_format({
            'font_size': 12,
            'valign': 'vcenter',
            'text_wrap': True,
            'border': 1
        })
        sheet.set_column('A:H', 15)

        header = [
            'Nama Pokemon',
            'Base HP',
            'Base Attack',
            'Base Defense',
            'Base Special Attack',
            'Base Special Defense',
            'Base Speed',
            'Type',
        ]
        sheet.write_row(0, 0, header, header_style)
        row = 1

        partner = self.env['res.partner'].search([])
        for rec in partner:
            data = []
            data.extend([
                rec.name,
                rec.base_hp,
                rec.base_attack,
                rec.base_defense,
                rec.base_special_attack,
                rec.base_special_defense,
                rec.base_speed,
                ' / '.join([types.name for types in rec.pokemon_type_ids])
            ])

            sheet.write_row(row, 0, data, text_style)
            row += 1