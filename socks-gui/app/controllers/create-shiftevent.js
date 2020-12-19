//import Controller from '@ember/controller';

//export default class CreateShifteventController extends Controller {
//}

import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default Route.extend({
  store: service(),
  setupController(controller, model) {
    this._super(controller, model);
    this.controller.set('form.date', '');
    this.controller.set('form.name', '');
    this.controller.set('form.role', '');
  },
  actions: {
    create() {
      const form = this.controller.get('form');
      const store = this.get('store');
      const newShiftEvent = store.createRecord('shiftevent', {
        date: form.date,
        name: form.name,
        role: form.role,
      });
      newShiftEvent.save()
        .then(() => {
          this.transitionTo('assign');
        });
     },
     cancel() {
       this.transitionTo('assign');
     }
  }
});
