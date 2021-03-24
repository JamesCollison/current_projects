using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Snake : MonoBehaviour
{   
    [SerializeField] SnakeSegment segment;
    [SerializeField] SnakeSegment head;
    [SerializeField] SnakeSegment tail;
    [SerializeField] int maxSize = 1;

    [Range(0.01f, 0.2f)][SerializeField] float deathTimer = 0.1f;

    SnakeSegment[] segments;
    Vector2 nextPos;
    int currentSize = 1;
    int sizeToAddOnEat = 1;

    GameController gameController;


    void Start()
    {
        SetInitialPosition();
        MakeInitialSegments();
        AddSegmentToParent(head);
        AddSegmentToParent(tail);
        SetGameController();
        StartCoroutine(SkipFirstFrame());
    }

    public void AddSegment(Vector2 direction)
    {
        MakeSegment(direction);
        CheckSizeOfSnake();
    }

    private void MakeSegment(Vector2 direction)
    {
        nextPos += direction;
        SnakeSegment nextSegment = Instantiate(segment, nextPos, Quaternion.identity);
        AddSegmentToParent(nextSegment);
        head.setNext(nextSegment);
        head = nextSegment;
        currentSize++;
    }

    private void CheckSizeOfSnake()
    {
        if (currentSize > maxSize)
        {
            RemoveTailOfSnake();
        }
    }

    private void RemoveTailOfSnake()
    {
        var currentTail = tail;
        tail = currentTail.GetNext();
        currentTail.RemoveTail();
        currentSize--;
    }

    private void AddSegmentToParent(SnakeSegment segment)
    {
        segment.transform.parent = transform;
    }

    public void AddLength(int n)
    {
        maxSize += sizeToAddOnEat;
        gameController.IncreaseScore(n);
        gameController.IncreaseStage(1);
        gameController.SetText();
    }

    private void MakeInitialSegments()
    {
        head = tail = Instantiate(segment, transform.position, transform.rotation);
    }

    public void PortalEntered()
    {
        gameController.IncreaseLevel();
    }

    public void SnakeDied()
    {
        gameController.GameOver();
        segments = FindObjectsOfType<SnakeSegment>();
        StartCoroutine(DeathSequence());
        gameController.SetGameOverScreen(true);
    }

    private void SetInitialPosition()
    {
        nextPos = transform.position;
    }

    private void SetGameController()
    {
        gameController = FindObjectOfType<GameController>();
    }

    float GetSpeed()
    {
        return gameController.GetSnakeSpeed();
    }

    IEnumerator DeathSequence()
    {
        foreach (SnakeSegment segment in segments)
        {
            segment.RemoveTail();
            yield return new WaitForSeconds(deathTimer);
        }
        Destroy(gameObject);
    }

    IEnumerator SkipFirstFrame()
    {
        // To avoid snake head and first snake segment from spawning on top of each other. 
        yield return new WaitForSeconds(GetSpeed());
        StartCoroutine(UpdateSnake());

    }

    IEnumerator UpdateSnake()
    {
        while (gameController.IsPlaying())
        {
            AddSegment(gameController.GetNextMove());
            yield return new WaitForSeconds(GetSpeed());
        }
    }
}
