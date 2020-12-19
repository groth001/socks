//import Controller from '@ember/controller';

//export default class CreateOooeventController extends Controller {
//}

import Controller from '@ember/controller';
import { computed } from '@ember/object';

export default Controller.extend({
  form: computed(function() {
    return {
      date: '',
      name: '',
      team: '',
      reason: ''
    }
  })
});
