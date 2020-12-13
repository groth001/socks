import EmberRouter from '@ember/routing/router';
import config from 'socks-gui/config/environment';

export default class Router extends EmberRouter {
  location = config.locationType;
  rootURL = config.rootURL;
}

Router.map(function() {
  this.route('login');
  this.route('authenticated', { path: '' }, function() {
    // all routes that require the session to be authenticated
    this.route('schedule');
    this.route('ooo', { path: '/out-of-office' });
    this.route('assign');
    this.route('reports');
  });
});
