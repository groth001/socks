//import Model from '@ember-data/model';

//export default class OooeventModel extends Model {

//}

import DS from 'ember-data';

export default DS.Model.extend({
  date: DS.attr(),
  name: DS.attr(),
  team: DS.attr(),
  reason: DS.attr(),
});
