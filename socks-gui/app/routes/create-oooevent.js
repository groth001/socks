//import Route from '@ember/routing/route';

//export default class CreateOooeventRoute extends Route {
//}

import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default Route.extend({
  store: service(),
  setupController(controller, model) {
    this._super(controller, model);
    this.controller.set('form.date', '');
    this.controller.set('form.name', '');
    this.controller.set('form.team', '');
    this.controller.set('form.reason', '');
  },
  actions: {
    create() {
      const form = this.controller.get('form');
      const store = this.get('store');
      const newOooEvent = store.createRecord('oooevent', {
        date: form.date,
        name: form.name,
        team: form.team,
        reason: form.reason,
      });
      newOooEvent.save()
        .then(() => {
          this.transitionTo('ooo');
        });
     },
     cancel() {
       this.transitionTo('ooo');
     }
  }
});
