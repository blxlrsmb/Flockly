/**
 * @license
 * Visual Blocks Editor
 *
 * Copyright 2012 Google Inc.
 * https://blockly.googlecode.com/
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * @fileoverview Variable blocks for Blockly.
 * @author fraser@google.com (Neil Fraser)
 */
'use strict';

goog.provide('Blockly.Blocks.facebook');

goog.require('Blockly.Blocks');

Blockly.Blocks['fb_getFriends'] = {
  init: function() {
    this.setColour(330);
    this.appendDummyInput()
        .appendField("My Facebook friend list");
    this.setOutput(true, 'Array');
  }
};

Blockly.Blocks['fb_updateStatus'] = {
    init: function() {
        this.setColour(123);
				this.appendValueInput('TEXT')
						.appendField('Update my status to');
        this.setPreviousStatement(true);
        this.setNextStatement(true);
    }
};

Blockly.Blocks['fb_commentStatus'] = {
	init: function() {
		this.setColour(123);
		this.appendValueInput('STATUS').appendField('Comment the status ');
		this.appendValueInput('TEXT').appendField('with: ');
		this.setPreviousStatement(true);
		this.setNextStatement(true);
		this.setInputsInline(true);
	}
};

Blockly.Blocks['fb_userInfo'] = {
    init: function() {
        this.setColour(123);
        var dropdown = new Blockly.FieldDropdown([
                ['The name of the user', 'name'],
                ['The sex of the user', 'sex'],
                ['The age of the user', 'age'],
                ['The id of the user', 'id'],
                ['The city of the user', 'city']]);
				this.appendValueInput('USER')
							.appendField(dropdown, 'FIELD');
        this.setOutput(true, 'TEXT');
        this.setInputsInline(true);
    }
};

Blockly.Blocks['fb_statusInfo'] = {
    init: function() {
        this.setColour(123);
        var dropdown = new Blockly.FieldDropdown([
                ['The time of the status', 'time'],
                ['The author of the status', 'author'],
                ['The content of the status', 'content'],
								['The id of the status', 'id'],
								['The location of the status', 'location']]);
				this.appendValueInput('STATUS')
						.appendField(dropdown, 'FIELD');
        this.setOutput(true, 'TEXT');
        this.setInputsInline(true);
    }
};

Blockly.Blocks['fb_getAllStatus'] = {
  init: function() {
    this.setColour(330);
    this.appendDummyInput()
        .appendField("List of new status from my friends");
    this.setOutput(true, 'Array');
  }
};

Blockly.Blocks['fb_getStatusOf'] = {
  init: function() {
    this.setColour(330);
    this.appendValueInput('USER')
        .appendField("List of new status from");
    this.setOutput(true, 'Array');
  }
};

/*
 *getFriendField =  function() {
 *  var friends = ['friend one', 'friend two'];
 *  var tmplist = [];
 *  friends.forEach(function(name) {
 *    tmplist.push([name, name]);
 *  });
 *  return new Blockly.FieldDropdown(tmplist);
 *};
 *
 *
 */
Blockly.Blocks['fb_user'] = {
	init: function() {
		this.setColour(330);
		var testdropdown = new Blockly.FieldDropdown([
			['haha', 'haha'],
			['hehe', 'hehe']]);
			this.appendValueInput('TEXT')
					.appendField(window.getFriendField(), "friend");
			this.setOutput(true, 'USER');
	}
};
