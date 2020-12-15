import { module, test } from 'qunit';
import { setupTest } from 'ember-qunit';

module('Unit | Route | assign', function(hooks) {
  setupTest(hooks);

  test('it exists', function(assert) {
    let route = this.owner.lookup('route:assign');
    assert.ok(route);
  });
});
