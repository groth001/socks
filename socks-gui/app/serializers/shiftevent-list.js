//import JSONAPISerializer from '@ember-data/serializer/json-api';

//export default class ShifteventListSerializer extends JSONAPISerializer {
//}

import DS from 'ember-data';

export default DS.JSONAPISerializer.extend({
  serialize(snapshot, options) {
    let json = this._super(...arguments);

    json.data = {
      type: 'shiftevent'
    };

    return json;
  },
});
