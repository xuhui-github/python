;Atom proides a way to manager shared,synchronous,independent state.They are
;a reference type like refs and vars.You create an atom with atom,and can 
;access its state with deref/@.Like refs and agents,atoms support validators.
;To change the value of an atom,you can use swap!.A lower-level 
;compare-and-set! is also provided.Changes to atoms are always free of race
;conditions

;While Vars ensure safe use of mutable storage locations via thread isolation, transactional
;
;references (Refs) ensure safe shared use of mutable storage locations via a software transactional
;
;memory (STM) system. Refs are bound to a single storage location for their lifetime, and only allow
;
;mutation of that location to occur within a transaction. In practise Refs are rarely used.
;
;Like Refs, Agents provide shared access to mutable state. Where Refs support coordinated,
;
;synchronous change of multiple locations, Agents provide independent, asynchronous change of
;
;individual locations. Agents are bound to a single storage location for their lifetime, and only allow
;
;mutation of that location (to a new state) to occur as a result of an action. Actions are functions
;
;(with, optionally, additional arguments) that are asynchronously applied to an Agent’s state and
;
;whose return value becomes the Agent’s new state. Because actions are functions they can also be
;
;multimethods and therefore actions are potentially polymorphic. Also, because the set of functions
;
;is open, the set of actions supported by an Agent is also open, a sharp contrast to pattern matching
;
;message handling loops provided by some other languages.
;
;Clojure’s Agents are reactive, not autonomous - there is no imperative message loop and no
;
;blocking receive. The state of an Agent should be itself immutable (preferably an instance of one of
;
;Clojure’s persistent collections), and the state of an Agent is always immediately available for
;
;reading by any thread (using the deref function or reader macro @) without any messages, i.e.
;
;observation does not require cooperation or coordination.
;
;Agent action dispatches take the form (send agent fn args*). send (and send-off) always returns
;
;immediately. At some point later, in another thread, the following will happen:
;
;• The given fn will be applied to the state of the Agent and the args, if any were supplied. The
;
;return value of the given fn will become the new state of the Agent.
;
;• If any watchers were added to the Agent, they will be called. See add-watch for details.
;
;• If during the function execution any other dispatches are made (directly or indirectly), they will
;
;be held until after the state of the Agent has been changed.
;
;• If any exceptions are thrown by an action function, no nested dispatches will occur, and the
;
;exception will be cached in the Agent itself. When an Agent has errors cached, any subsequent
;
;interactions will immediately throw an exception, until the agent’s errors are cleared. Agent
;
;errors can be examined with agent-error and the agent restarted with restart-agent.
;
;The actions of all Agents get interleaved amongst threads in a thread pool. At any point in time, at
;
;most one action for each Agent is being executed. Actions dispatched to an agent from another
;
;single agent or thread will occur in the order they were sent, potentially interleaved with actions
;
;dispatched to the same agent from other sources. send should be used for actions that are CPU
;
;limited, while send-off is appropriate for actions that may block on IO.
;
;Agents are integrated with the STM - any dispatches made in a transaction are held until it commits,
;
;and are discarded if it is retried or aborted. No user-code locking is involved.
;
;Note that use of Agents starts a pool of non-daemon background threads that will prevent
;
;shutdown of the JVM. Use shutdown-agents to terminate these threads and allow shutdown.
;
