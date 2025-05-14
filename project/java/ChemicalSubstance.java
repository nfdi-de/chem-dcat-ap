package None;

import java.util.List;
import lombok.*;






/**
  A portion of matter of constant composition, composed of molecular entities of the same type or of different types that is being evaluated in a scientific process.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ChemicalSubstance extends EvaluatedEntity {

  private List<ChemicalEntity> composedOf;

}