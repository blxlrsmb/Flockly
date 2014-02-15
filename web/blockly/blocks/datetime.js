//File: datetime.js
//Date: Sat Feb 15 15:18:19 2014 +0800
//Author: Yuxin Wu <ppwwyyxxc@gmail.com>


'use strict';
goog.provide('Blockly.Blocks.datetime');

goog.require('Blockly.Blocks');

Blockly.Blocks['time_field'] = {
	init: function() {
		this.setColour(150);
		var dropdown = new Blockly.FieldDropdown(window.duplicateList(
			['year', 'month', 'day', 'hour', 'minute', 'second']
		));
		this.appendValueInput('DATETIME')
				.appendField(dropdown, 'FIELD')
				.appendField("of the time");
		this.setOutput(true, 'Number');
	}
};
