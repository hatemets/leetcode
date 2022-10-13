const util = require("util") 

/**
Description:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Examples:
1) Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

2) Input: list1 = [], list2 = []
Output: []
**/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */

function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}


const mergeTwoLists = (list1, list2) => {
    if (!list1 && !list2) {
        return
    }
    let merged = new ListNode()
    let head = new ListNode()
    let firstRound = true
    let run = true

    while (run) {
        if (list1 && !list2) {
            merged.val = list1.val
            list1 = list1.next
        }
        else if (list2 && !list1) {
            merged.val = list2.val
            list2 = list2.next
        }
        else {
            if (list1.val <= list2.val) {
                merged.val = list1.val
                list1 = list1.next
            }
            else {
                merged.val = list2.val
                list2 = list2.next
            }
        }


        if (firstRound) {
            firstRound = false
            head = merged
        }

        if (!list1 && !list2) {
            run = false
        }
        else {
            merged.next = new ListNode()
            merged = merged.next
        }
    }

    return head
}

// List 1
const a5 = new ListNode(19)
const a4 = new ListNode(13, a5)
const a3 = new ListNode(7, a4)
const a2 = new ListNode(5, a3)
const a1 = new ListNode(1, a2)

// List 1
const b4 = new ListNode(25)
const b3 = new ListNode(9, b4)
const b2 = new ListNode(3, b3)
const b1 = new ListNode(2, b2)

// console.log(util.inspect(mergeTwoLists(a1, b1), false, null))
const x1 = new ListNode()
const x2 = new ListNode()
// console.log(util.inspect(mergeTwoLists(x1, x2), false, null))









const list1 = new ListNode("")
const list2 = new ListNode(0)

console.log(list1)
console.log(list2)
