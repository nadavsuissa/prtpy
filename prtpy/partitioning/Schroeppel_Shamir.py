"""
Optimally Scheduling Small Numbers of Identical Parallel Machines,
by ichard E.Korf and Ethan L. Schreiber (2013) https://ojs.aaai.org/index.php/ICAPS/article/view/13544
Yoel Chemla
"""
import doctest

from prtpy.partitioning.MaxHeap import MaxHeap
from prtpy.partitioning.MinHeap import MinHeap
from prtpy.partitioning.Horowitz_And_Sahni import poewer_set


def schroeppel_shamir(s):
    """
        Algorithm 2: get a list, return list that contain all the pair from the groups partiroins.
        This algorithm help to algorithm1 with the partition.

        >>> schroeppel_shamir([1, 2, 3])
        ([[0, 0], [0, 1]], [[2, 3], [2, 0], [0, 3], [0, 0]])
    """

    # sort s in decrease order
    sorted(s, reverse=True)

    # divide to 4 subset sum

    left_sum = s[:len(s) // 2]
    right_sum = s[len(s) // 2:]

    # divide to 4 subset sum
    a0 = left_sum[:len(left_sum) // 2]
    a1 = left_sum[len(left_sum) // 2:]
    b0 = right_sum[:len(right_sum) // 2]
    b1 = right_sum[len(right_sum) // 2:]
    
    subset_sum_a0 = poewer_set(a0)
    subset_sum_a1 = poewer_set(a1)
    subset_sum_b0 = poewer_set(b0)
    subset_sum_b1 = poewer_set(b1)
   

    list_of_sum_a0 = [sum(subset_sum_a0[i]) for i in range(len(subset_sum_a0))]

    list_of_sum_a1 = [sum(subset_sum_a1[i]) for i in range(len(subset_sum_a1))]

    list_of_sum_b0 = [sum(subset_sum_b0[i]) for i in range(len(subset_sum_b0))]

    list_of_sum_b1 = [sum(subset_sum_b1[i]) for i in range(len(subset_sum_b1))]

    #  increase
    list_of_sum_a0.sort()
    list_of_sum_a1.sort()

    #  decrease
    list_of_sum_b0.sort(reverse=True)
    list_of_sum_b1.sort(reverse=True)

    # merge
    list_sorted1 = [[list_of_sum_a0[i], list_of_sum_a1[j]] for i in range(len(list_of_sum_a0)) for j in range(len(list_of_sum_a1))]
    
    min_heap = MinHeap()
    for i in list_sorted1:
        min_heap.push(i)
 
    list_sorted2 = [[list_of_sum_b0[i], list_of_sum_b1[j]] for i in range(len(list_of_sum_b0)) for j in range(len(list_of_sum_b1))]
    max_heap = MaxHeap()
    for i in list_sorted2:
        max_heap.push(i)

    return min_heap.heap, max_heap.heap


if __name__ == '__main__':
    doctest.testmod()
