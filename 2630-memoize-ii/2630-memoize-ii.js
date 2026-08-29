/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const cache = new Map();

    return function (...args) {
        let current = cache;

        for (const arg of args) {
            if (!current.has(arg)) {
                current.set(arg, new Map());
            }

            current = current.get(arg);
        }

        if (current.has("__result__")) {
            return current.get("__result__");
        }

        const result = fn(...args);

        current.set("__result__", result);

        return result;
    };
}