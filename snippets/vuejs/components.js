import Vue from 'vue'
import upperFirst from 'lodash/upperFirst'
import camelCase from 'lodash/camelCase'

// Pega todos os componentes da pasta '@/components' e os registra globalmente

const pascalCase = text => upperFirst(camelCase(text))

const removeFileExtension = name => name.replace(/^\.\/(.*)\.\w+$/, '$1')

const components = require.context('@/components', false, /\.(vue|js)$/)

components.keys().forEach(fileName => {
  const componentConfig = components(fileName)
  const componentName = pascalCase(removeFileExtension(fileName))

  Vue.component(componentName, componentConfig.default || componentConfig)
})
