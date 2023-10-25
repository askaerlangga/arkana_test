/** @odoo-module */
import { ListController } from "@web/views/list/list_controller";
import { registry } from '@web/core/registry';
import { listView } from '@web/views/list/list_view';
export class ResPartnerButtonListController extends ListController {
    setup() {
        super.setup();
    }
    OnFetchButtonClick() {
        var rpc = require('web.rpc');
        rpc.query({
            model: 'res.partner',
            method: 'fetch_pokemon_action',
            args: [""]
        }).then();
    }

    OnPrintButtonClick() {
        this.actionService.doAction("ae_contact.pokemon_xlsx_action")
    }
}
registry.category("views").add("button_in_tree", {
    ...listView,
    Controller: ResPartnerButtonListController,
    buttonTemplate: "res_partner.ListView.Buttons",
});