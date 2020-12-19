//import Model from '@ember-data/model';

//export default class ShifteventDetailModel extends Model {

//}

import DS from 'ember-data';

export default DS.Model.extend({
  date: DS.attr(),
  name: DS.attr(),
  role: DS.attr(),
});
