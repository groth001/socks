//import JSONAPIAdapter from '@ember-data/adapter/json-api';

//export default class ApplicationAdapter extends JSONAPIAdapter {
import DS from 'ember-data';
import ENV from '../config/environment';
import { computed } from '@ember/object';

export default DS.JSONAPIAdapter.extend({
  host: computed(function(){
    return ENV.API_HOST;
  }),

  namespace: 'api'
});
//}
