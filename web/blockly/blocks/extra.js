//File: extra.js
//Date: Sat Feb 15 17:21:09 2014 +0800
//Author: Yuxin Wu <ppwwyyxxc@gmail.com>


// added
Blockly.Blocks['text_include'] = {
  init: function() {
    this.setColour(160);
    this.setOutput(true, 'Boolean');
    this.appendValueInput('VALUE')
        .setCheck('String').appendField("text");
    this.appendValueInput('FIND')
        .setCheck('String').appendField("is part of text");

    if (Blockly.Msg.TEXT_INDEXOF_TAIL) {
      this.appendDummyInput().appendField(Blockly.Msg.TEXT_INDEXOF_TAIL);
    }
    this.setInputsInline(true);
  }
};
