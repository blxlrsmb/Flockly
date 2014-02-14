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


Blockly.Blocks['fb_userInfo'] = {
    init: function() {
        this.setColour(123);
        var dropdown = new Blockly.FieldDropdown([
                ['The name of the user', 'NAME'],
                ['The sex of the user', 'SEX'],
                ['The age of the user', 'AGE'],
                ['The id of the user', 'ID'],
                ['The city of the user', 'CITY']]);
				this.appendValueInput('USER')
						.appendField(dropdown, 'END');
        this.setOutput(true, 'TEXT');
        this.setInputsInline(true);
    }
};
