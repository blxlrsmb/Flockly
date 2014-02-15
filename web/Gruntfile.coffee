module.exports = (grunt) ->
  'use strict'

  grunt.initConfig
    pkg: grunt.file.readJSON('package.json')

    coffee:
      dev:
        files: [
          expand: true
          cwd: 'js'
          src: ['**/*.coffee', '!**/_*.coffee']
          dest: 'build/js'
          ext: '.js'
        ]

    sass:
      dev:
        options:
          loadPath: 'bower_components/foundation/scss'
        files: [
          expand: true
          cwd: 'css'
          src: ['**/*.sass', '!**/_*.sass']
          dest: 'build/css'
          ext: '.css'
        ]

    slim:
      dev:
        files: [
          expand: true
          src: ['*.slim', '!_*.slim']
          dest: 'build'
          ext: '.html'
        ]

    watch:
      options:
        livereload: true
        spawn: false

      coffee:
        files: ['js/**/*.coffee']
        tasks: ['coffee:dev']

      sass:
        files: ['css/**/*.sass']
        tasks: ['sass:dev']

      slim:
        files: ['*.slim']
        tasks: ['slim:dev']

    connect:
      dev:
        options:
          port: 9999
          host: 'localhost'
          base: 'build'
          livereload: true
          open: true

    clean:
      dev: ['build/*']

    bower:
      dev:
        options:
          targetDir: 'vendor/assets'
          layout: 'byType'

  grunt.loadNpmTasks 'grunt-bower-task'
  grunt.loadNpmTasks 'grunt-contrib-coffee'
  grunt.loadNpmTasks 'grunt-contrib-connect'
  grunt.loadNpmTasks 'grunt-contrib-sass'
  grunt.loadNpmTasks 'grunt-contrib-watch'
  grunt.loadNpmTasks 'grunt-slim'

  grunt.registerTask 'dev', ['coffee:dev', 'sass:dev', 'slim:dev']
  grunt.registerTask 'default', ['dev', 'connect', 'watch']
