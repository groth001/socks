import OAuth2PasswordGrant from 'ember-simple-auth/authenticators/oauth2-password-grant';
import ENV from '../config/environment';

export default class OAuth2Authenticator extends OAuth2PasswordGrant {
  this.serverTokenEndpoint = ENV.API_HOST;
};
