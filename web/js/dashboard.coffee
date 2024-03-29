## Functions

renameTag = (node, name) ->
  unless node.jquery
    node = $(node)
  node2 = $('<'+name+'/>').html node.html()
  node.replaceWith node2
  node2

## Main

$.ajaxSetup error: -> location.replace '/'

Flockly.getProfile (data, status, xhr) ->
  $('.profile-picture').css 'background-image', "url(#{data.picture.data.url})"
  $('.profile-name').text data.name

$('#logout').on 'click', ->
  window.location.href = '/logout'

$('#search-input').on 'input', ->
  needle = new RegExp($(@).val(), 'i')
  $('#blocks ol').each (_, el) ->
    el.style.display = ''
    renameTag el, 'li'
  $('#blocks li').each (_, el) ->
    unless $('.block-name', el).text().match needle
      x = renameTag(el, 'ol')
      x[0].style.display = 'none'

$file = $('#xml-file')
$file.on 'change', ->
  if @.files.length > 0
    r = new FileReader
    r.onload = (e) ->
      $.post '/upload_blockly', {content: e.target.result, name: 'New Block'}, ->
        location.reload()
    r.readAsText @.files[0]
    @.value = null
$('#import-xml').on 'click', (ev) ->
  ev.preventDefault()
  $file.trigger 'click'

Handlebars.registerHelper 'fmtTime', (epoch, options) ->
  moment((+epoch)*1000).format 'YYYY-MM-DD hh:mm'
blockItemTpt = Handlebars.compile $('#block-item-tpt').html()

$.getJSON '/get_blockly_list', (data) ->
  data.forEach (item) ->
    $('#blocks').append $('<li/>').html blockItemTpt item

$(document).on 'click', '.switch-on, .switch-off', ->
  if $(@).hasClass 'switch-on'
    enabled = 1
    $(@).removeClass 'switch-on'
    $(@).addClass 'switch-off'
  else
    enabled = 0
    $(@).removeClass 'switch-off'
    $(@).addClass 'switch-on'
  $('input', @).prop 'checked', ! $('input', @).prop('checked')
  $.get "/enable?id=#{$(@).parent().data('id')}&enabled=#{1-enabled}"
