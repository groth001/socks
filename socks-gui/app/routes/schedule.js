import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

//export default class ScheduleRoute extends Route {
export default Route.extend({
  store: service(),
  async model() {
    let response;
    let store;

    store = this.get('store');
    response = await store.findAll('shiftevent');

    return response;
  }
//  @service store;

//  async model() {
//    return this.store.findAll('shiftevent');
});
