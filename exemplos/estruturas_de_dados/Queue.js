export default class Queue {
    constructor () {
        this.elements = [ ...arguments ]
    }

    insert (value) {
        this.elements.push(value)
        return this
    }

    remove () {
        this.elements.shift()
        return this
    }

    get firstElement () {
        return this.elements[0]
    }

    get length () {
        return this.elements.length
    }
}
