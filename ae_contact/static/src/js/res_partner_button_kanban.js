/** @odoo-module */
import { KanbanController } from "@web/views/kanban/kanban_controller";
import { registry } from '@web/core/registry';
import { kanbanView } from '@web/views/kanban/kanban_view';
export class ResPartnerButtonKanbanController extends KanbanController {
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
registry.category("views").add("button_in_kanban", {
    ...kanbanView,
    Controller: ResPartnerButtonKanbanController,
    buttonTemplate: "res_partner.KanbanView.Buttons",
});