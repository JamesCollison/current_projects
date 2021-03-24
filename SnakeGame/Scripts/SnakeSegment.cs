using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SnakeSegment : MonoBehaviour
{
    [SerializeField] SnakeSegment next;
    Snake snake;


    void Start()
    {
        snake = FindObjectOfType<Snake>();
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        switch (collision.tag)
        {
            case "Snake":
                Kill();
                break;
            case "Walls":
                Kill();
                break;
            case "Points":
                Eat(collision);
                break;
            case "Portal":
                LevelController levelLoader = FindObjectOfType<LevelController>();
                levelLoader.LoadNextLevel();
                snake.PortalEntered();
                break;
        }
    }

    void Eat(Collider2D collision)
    {
        var points = collision.GetComponent<PointObject>().GetPoints();
        snake.AddLength(points);
        Destroy(collision.gameObject);
    }

    public void setNext(SnakeSegment segment)
    {
        next = segment;
    }

    public SnakeSegment GetNext()
    {
        return next;
    }

    public void Kill()
    {
        snake.SnakeDied();
    }

    public void RemoveTail()
    {
        Destroy(gameObject);
    }
}
