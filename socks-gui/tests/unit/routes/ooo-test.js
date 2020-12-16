import { module, test } from 'qunit';
import { setupTest } from 'ember-qunit';

module('Unit | Route | ooo', function(hooks) {
  setupTest(hooks);

  test('it exists', function(assert) {
    let route = this.owner.lookup('route:ooo');
    assert.ok(route);
  });
});
