'use strict'

var util = require('util');
var Transform = require('stream').Transform;

module.exports = ToString;

util.inherits(ToString, Transform);

function ToString(options) {
  if (!(this instanceof ToString)) {
    return new ToString(options);
  }
  Transform.call(this, options);
}

ToString.prototype._transform = function (data, enc, cb) {
  this.push(data.toString('utf8'));
  cb();
};
