Flockly.getProfile (data, status, xhr) ->
  location.replace '/dashboard'
, ->
  console.log 'not logged in'

$('#login').on 'click', (e) ->
  window.location.href = '/auth'
