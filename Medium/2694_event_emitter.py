"""
2694. Event Emitter

Design an EventEmitter class. This interface is similar (but with some differences) to the
one found in Node.js or the Event Target interface of the DOM. The EventEmitter should allow
for subscribing to events and emitting them.

Your EventEmitter class should have the following two methods:

- subscribe - This method takes in two arguments: the name of an event as a string and a callback
function. This callback function will later be called when the event is emitted.
An event should be able to have multiple listeners for the same event. When emitting an event with
multiple callbacks, each should be called in the order in which they were subscribed. An array
of results should be returned. You can assume no callbacks passed to subscribe are referentially
identical.
The subscribe method should also return an object with an unsubscribe method that enables the user
to unsubscribe. When it is called, the callback should be removed from the list of subscriptions
and undefined should be returned.

- emit - This method takes in two arguments: the name of an event as a string and an optional
array of arguments that will be passed to the callback(s). If there are no callbacks subscribed
to the given event, return an empty array. Otherwise, return an array of the results of all callback
calls in the order they were subscribed.
"""

"""
Example 1:
Input: 
actions = ["EventEmitter", "emit", "subscribe", "subscribe", "emit"], 
values = [[], ["firstEvent"], ["firstEvent", "function cb1() { return 5; }"],  
["firstEvent", "function cb1() { return 6; }"], ["firstEvent"]]
Output: [[],["emitted",[]],["subscribed"],["subscribed"],["emitted",[5,6]]]

Explanation: 
const emitter = new EventEmitter();
emitter.emit("firstEvent"); // [], no callback are subscribed yet
emitter.subscribe("firstEvent", function cb1() { return 5; });
emitter.subscribe("firstEvent", function cb2() { return 6; });
emitter.emit("firstEvent"); // [5, 6], returns the output of cb1 and cb2

Example 2:
Input: 
actions = ["EventEmitter", "subscribe", "emit", "emit"], 
values = [[], ["firstEvent", "function cb1(...args) { return args.join(','); }"],
["firstEvent", [1,2,3]], ["firstEvent", [3,4,6]]]
Output: [[],["subscribed"],["emitted",["1,2,3"]],["emitted",["3,4,6"]]]

Explanation: Note that the emit method should be able to accept an OPTIONAL array of arguments.
const emitter = new EventEmitter();
emitter.subscribe("firstEvent, function cb1(...args) { return args.join(','); });
emitter.emit("firstEvent", [1, 2, 3]); // ["1,2,3"]
emitter.emit("firstEvent", [3, 4, 6]); // ["3,4,6"]

Example 3:
Input: 
actions = ["EventEmitter", "subscribe", "emit", "unsubscribe", "emit"], 
values = [[], ["firstEvent", "(...args) => args.join(',')"], ["firstEvent", [1,2,3]], [0],
["firstEvent", [4,5,6]]]
Output: [[],["subscribed"],["emitted",["1,2,3"]],["unsubscribed",0],["emitted",[]]]

Explanation:
const emitter = new EventEmitter();
const sub = emitter.subscribe("firstEvent", (...args) => args.join(','));
emitter.emit("firstEvent", [1, 2, 3]); // ["1,2,3"]
sub.unsubscribe(); // undefined
emitter.emit("firstEvent", [4, 5, 6]); // [], there are no subscriptions

Example 4:
Input: 
actions = ["EventEmitter", "subscribe", "subscribe", "unsubscribe", "emit"], 
values = [[], ["firstEvent", "x => x + 1"], ["firstEvent", "x => x + 2"], [0], ["firstEvent", [5]]]
Output: [[],["subscribed"],["subscribed"],["unsubscribed",0],["emitted",[7]]]

Explanation:
const emitter = new EventEmitter();
const sub1 = emitter.subscribe("firstEvent", x => x + 1);
const sub2 = emitter.subscribe("firstEvent", x => x + 2);
sub1.unsubscribe(); // undefined
emitter.emit("firstEvent", [5]); // [7]
"""

class EventEmitter:
    def __init__(self):
        self.events = {} # used to store event (callback, active) pairs

    def subscribe(self, event_name, callback):
        if event_name not in self.events:
            self.events[event_name] = [] # initializing
        record = [callback, True]
        self.events[event_name].append(record)

        def unsubscribe():
            record[1] = False

        return unsubscribe

    def emit(self, event_name, args=None):
        if args is None:
            args = []
        results = []
        for record in self.events.get(event_name, []):
            callback, active = record
            if active:
                results.append(callback(*args))
        return results

class EventEmitter:
    def __init__(self):
        self._events = {}

    def subscribe(self, event_name: str, callback):
        if event_name not in self._events:
            self._events[event_name] = []

        self._events[event_name].append(callback)

        class Subscription:
            def __init__(self, events, name, cb):
                self._events = events
                self._name = name
                self._cb = cb

            def unsubscribe(self):
                lst = self._events.get(self._name, [])
                if self._cb in lst:
                    lst.remove(self._cb)

        return Subscription(self._events, event_name, callback)

    def emit(self, event_name: str, args=None):
        if args is None:
            args = []

        callbacks = self._events.get(event_name, [])
        return [cb(*args) for cb in callbacks]
