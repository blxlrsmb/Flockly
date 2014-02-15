//File: datetime.js
//Date: Sat Feb 15 18:35:38 2014 +0800
//Author: Yuxin Wu <ppwwyyxxc@gmail.com>


'use strict';
goog.provide('Blockly.Blocks.datetime');

goog.require('Blockly.Blocks');

Blockly.Blocks['time_field'] = {
	init: function() {
		this.setColour(150);
		var dropdown = new Blockly.FieldDropdown(window.blocklyTool.duplicateList(
			['year', 'month', 'day', 'hour', 'minute', 'second']
		));
		this.appendValueInput('DATETIME')
				.appendField(dropdown, 'FIELD')
				.appendField("of the time");
		this.setOutput(true, 'Number');
	}
};

Blockly.Blocks['time_time'] = {
	init: function() {
		this.setColour(150);
		this.appendDummyInput()
			.appendField('time')
			.appendField(new Blockly.FieldTextInput('2014'), 'YEAR')
			.appendField('-')
			.appendField(new Blockly.FieldTextInput('1'), 'MONTH')
			.appendField('-')
			.appendField(new Blockly.FieldTextInput('1'), 'DAY')
			.appendField(' ')
			.appendField(new Blockly.FieldTextInput('0'), 'HOUR')
			.appendField(':')
			.appendField(new Blockly.FieldTextInput('0'), 'MINUTE')
		this.setInputsInline(true);
		this.setOutput(true, 'DATETIME');
	}
};

Blockly.Blocks['time_lastTimeExecuted'] = {
	init: function() {
		this.setColour(150);
		this.setOutput(true, 'DATETIME');
		this.appendDummyInput().
			appendField("Last time this program was executed");
	}
};

Blockly.Blocks['time_totTimesExecuted'] = {
	init: function() {
		this.setColour(150);
		this.setOutput(true, 'Number');
		this.appendDummyInput().
			appendField("Total times this program has been executed");
	}
};

Blockly.Blocks['time_currentTime'] = {
	init: function() {
		this.setColour(150);
		this.setOutput(true, 'DATETIME');
		this.appendDummyInput().
			appendField("Current time");
	}
}
