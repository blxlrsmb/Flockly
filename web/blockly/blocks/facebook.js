//File: facebook.js
//Date: Sat Feb 15 15:12:18 2014 +0800
//Author: Yuxin Wu <ppwwyyxxc@gmail.com>

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

Blockly.Blocks['fb_user'] = {
	init: function() {
		this.setColour(330);
		this.appendDummyInput()
				.appendField(window.getFriendField(), "friend");
		this.setOutput(true, 'USER');
	}
};
