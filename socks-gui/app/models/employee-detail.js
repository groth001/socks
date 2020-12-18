//import Model from '@ember-data/model';

//export default class EmployeeDetailModel extends Model {

//}

import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr(),
  email: DS.attr(),
  team: DS.attr(),
  rank: DS.attr(),
  shift: DS.attr(),
});
