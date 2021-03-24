using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class TextManager : MonoBehaviour
{
    [SerializeField] Text scoreText;
    [SerializeField] Text levelText;
    [SerializeField] Text stageText;


    public void setScoreText(int value)
    {
        scoreText.text = value.ToString();
    }
    public void setLevelText(int value)
    {
        levelText.text = value.ToString();
    }
    public void setStageText(int value)
    {
        stageText.text = value.ToString();
    }
}
